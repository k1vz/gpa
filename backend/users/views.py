from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
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
	def post(self, req):
		user = User.objects.filter(email=req.data['email']).first()

		if user is None:
			raise AuthenticationFailed('Email não encontrado')

		if not user.check_password(req.data['password']):
			raise AuthenticationFailed('Senha incorreta')

		payload = {
			'id': user.id,
			'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
			'iat': datetime.datetime.utcnow()
		}

		token = jwt.encode(payload, 'secret', algorithm='HS256')

		res = Response()
		res.set_cookie(key='jwt', value=token, httponly=True)
		res.data = {
			'jwt': token
		}

		return res

class UserDetailView(APIView):
	def get(self, req, pk):
		token = req.COOKIES.get('jwt')

		if not token:
			raise AuthenticationFailed('Não autorizado')

		try:
			payload = jwt.decode(token, 'secret', algorithms=['HS256'])
		except jwt.ExpiredSignatureError:
			raise AuthenticationFailed('Não autorizado')

		if pk:
			user = User.objects.filter(id=pk).first()
		else:
			user = User.objects.filter(id=payload['id']).first()
		serializer = UserSerializer(user)

		return Response(serializer.data)


# class ClientDetailView(APIView):
# 	def get_object(self, pk):
# 		try:
# 			return Client.objects.get(pk=pk)
# 		except Client.DoesNotExist:
# 			raise NotFound('Client não encontrado')

# 	def get(self, req, pk):
# 		client = self.get_object(pk)
# 		serializer = ClientSerializer(client)

# 		return Response(serializer.data)

# 	def put(self, req, pk):
# 		client = self.get_object(pk)

# 		serializer = ClientSerializer(client, data=req.data)
# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()

# 		return Response(serializer.data)

# 	def patch(self, req, pk):
# 		client = self.get_object(pk)

# 		serializer = ClientSerializer(client, data=req.data, partial=True)
# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()

# 		return Response(serializer.data)

# 	def delete(self, req, pk):
# 		client = self.get_object(pk)
# 		client.delete()

# 		return Response(status=status.HTTP_204_NO_CONTENT)
	
class UserLogoutView(APIView):
	def get(self, req):
		res = Response()
		res.delete_cookie('jwt')
		res.data = {
			'message': 'success'
		}

		return res