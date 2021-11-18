from requests import post
from flask import abort

def is_authenticated(request):
  """
  Verify auth token
  """
  token = request.headers.get('authentication-token', None)
  validation = post(
    'http://localhost:5001/api/token/validate', 
    headers={'authentication-token': token}
  )

  if validation.status_code != 200:
    return abort(401, 'Invalid authentication token')
    