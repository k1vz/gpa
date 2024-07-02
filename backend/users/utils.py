import jwt
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import AuthenticationFailed

def getPayload(req):
	token = req.COOKIES.get('jwt')

	if not token:
		raise AuthenticationFailed('Not authorized')

	try:
		payload = jwt.decode(token, 'secret', algorithms=['HS256'])
	except jwt.ExpiredSignatureError:
		raise AuthenticationFailed('Not authorized')

	return payload

def getUser(id, pk):
	if pk:
		user = get_object_or_404(User, id=pk)
	else:
		user = get_object_or_404(User, id=id)

	return user
