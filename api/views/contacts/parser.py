from flask import abort
from api.utils.auth import is_authenticated
from api.utils.format import parse_customer


def parser(request):
  validation = is_authenticated(request)

  if not request.json.get('name'):
    return abort(400, 'Missing name field')

  if not request.json.get('cellphone'):
    return abort(400, 'Missing cellphone field')

  if not request.headers.get('authentication-token'):
    return abort(401, 'Missing authentication-token header')
    
  return {
    'nome': request.json.get('name'),
    'celular': request.json.get('cellphone'),
    'cliente': parse_customer(validation.get('email'))  
  }