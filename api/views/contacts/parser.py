from flask import abort
from api.utils.auth import is_authenticated


def parser(request):
  if not request.json.get('name'):
    return abort(400, 'Missing name field')

  if not request.json.get('cellphone'):
    return abort(400, 'Missing cellphone field')

  if not request.json.get('customer'):
    return abort(400, 'Missing customer field')

  if not request.headers.get('authentication-token'):
    return abort(401, 'Missing authentication-token header')

  is_authenticated(request)

  return {
    'nome': request.json.get('name'),
    'celular': request.json.get('cellphone'),
    'cliente': request.json.get('customer')  
  }