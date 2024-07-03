from django.forms import ValidationError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserSerializer
from .utils import getUser, getPayload
from .models import User
import jwt, datetime

class UserListView(APIView):
	def get(self, req):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)

		return Response(serializer.data)

class UserRegisterView(APIView):
	def post(self, req):
		serializer = UserSerializer(data=req.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data)

class UserLoginView(APIView):
	def get(self, req):
		return render(req, 'login.html')

	def post(self, req):
		user = get_object_or_404(User, email=req.data['email'])

		if not user.check_password(req.data['password']):
			return JsonResponse({'error': 'Not authorized'}, status=401)

		payload = {
			'id': user.id,
			'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
			'iat': datetime.datetime.utcnow()
		}

		token = jwt.encode(payload, 'secret', algorithm='HS256')

		res = redirect('home')
		res.set_cookie(key='jwt', value=token, httponly=True)
	
		return res

class UserDetailView(APIView):
	def get(self, req, pk):
		payload = getPayload(req)
		user = getUser(payload['id'], pk)
		
		serializer = UserSerializer(user)

		return Response(serializer.data)

class UserUpdateView(APIView):
	def put(self, req):
		payload = getPayload(req)
		user = get_object_or_404(User, id=payload['id'])

		data = req.data
		email = data.get('email')
		current_password = data.get('current_password')
		new_password = data.get('new_password')

		if current_password and not user.check_password(current_password):
			raise ValidationError("Incorrect current password")

		if email:
			user.email = email

		if new_password:
			if current_password:
				user.set_password(new_password)
			else:
				raise ValidationError("Current password is needed to create a new password")

		user.save()
		serializer = UserSerializer(user)

		return Response(serializer.data, status=status.HTTP_200_OK)


class UserDeleteView(APIView):
	def delete(self, req, pk):
		payload = getPayload(req)
		user = getUser(payload['id'], pk)
		user.delete()

		return Response(status=status.HTTP_204_NO_CONTENT)

class UserLogoutView(APIView):
	def get(self, req):
		res = redirect('user-login')
		res.delete_cookie('jwt')

		return res