from flask_restful import Api

from api.views.contacts.view import ContactView

def routes(api: Api):
  api.add_resource(ContactView, '/contacts')
