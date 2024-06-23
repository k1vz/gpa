from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from .serializers import UserSerializer
import jwt, datetime

class RegisterView(APIView):
	def post(self, req):
		serializer = UserSerializer(data=req.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response(serializer.data)

class LoginView(APIView):
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

class UserView(APIView):
	def get(self, req):
		token = req.COOKIES.get('jwt')

		if not token:
			raise AuthenticationFailed('Não autorizado')

		try:
			payload = jwt.decode(token, 'secret', algorithms=['HS256'])
		except jwt.ExpiredSignatureError:
			raise AuthenticationFailed('Não autorizado')

		user = User.objects.filter(id=payload['id']).first()
		serializer = UserSerializer(user)

		return Response(serializer.data)

class LogoutView(APIView):
	def get(self, req):
		res = Response()
		res.delete_cookie('jwt')
		res.data = {
			'message': 'success'
		}

		return res