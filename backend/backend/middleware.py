from django.http import JsonResponse
import jwt
from rest_framework.exceptions import AuthenticationFailed
from django.utils.deprecation import MiddlewareMixin

class AuthMiddleware(MiddlewareMixin):
	def process_request(self, req):
		excluded_paths = ['/users/register/', '/users/login/']

		if req.path in excluded_paths:
			return

		token = req.COOKIES.get('jwt')

		if not token:
			return JsonResponse({'error': 'Não autorizado'}, status=401)

		try:
			jwt.decode(token, 'secret', algorithms=['HS256'])
		except jwt.ExpiredSignatureError:
			return JsonResponse({'error': 'Não autorizado'}, status=401)
