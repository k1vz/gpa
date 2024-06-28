from django.shortcuts import get_object_or_404
import jwt
from rest_framework.exceptions import AuthenticationFailed
from .models import User

def isAuth(req):
	print(req, 'UTILS')
	token = req.COOKIES.get('jwt')

	if not token:
		raise AuthenticationFailed('Não autorizado')

	try:
		payload = jwt.decode(token, 'secret', algorithms=['HS256'])
	except jwt.ExpiredSignatureError:	
		raise AuthenticationFailed('Não autorizado')
	
	return payload

def getUser(id, pk):
	if pk:
		user = get_object_or_404(User, id=pk)
	else:
		user = get_object_or_404(User, id=id)

	return user