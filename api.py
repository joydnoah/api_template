# External packages
from flask_restful import Api

from resources.check_resource import CheckResource

def set_up_api(app):
    api = Api(app)

    api.add_resource(CheckResource, '/')