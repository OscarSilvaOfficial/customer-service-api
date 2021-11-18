from flask import request
from flask.views import MethodView
from api.models.varejao import Varejao
from api.utils.request import parse_request
from api.views.contacts.parser import parser
from api.models.macapa import Macapa


class ContactView(MethodView):

  def __init__(self) -> None:
    super().__init__()

  @parse_request(request, parser)
  def post(self, request):
    client = request.get('cliente')
    request.pop('cliente')
    clients = {
      'macapa': Macapa,
      'varejao': Varejao,
    }

    contact = clients[client](**request).save()

    return contact.to_dict() 