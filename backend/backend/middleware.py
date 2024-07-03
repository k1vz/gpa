from django.http import JsonResponse
from django.shortcuts import redirect
import jwt
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleware(MiddlewareMixin):
	def process_request(self, req):
		excluded_paths = ['/users/register/', '/users/login/', '/users/logout/']

		if req.path in excluded_paths:
			return

		token = req.COOKIES.get('jwt')

		if not token:
			print('i')
			return redirect('user-login')

		try:
			jwt.decode(token, 'secret', algorithms=['HS256'])
		except jwt.ExpiredSignatureError:
			return redirect('user-login')
