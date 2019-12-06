from flask_restful import Resource
from flask import jsonify

class CheckResource(Resource):
    """
    Check API Endpoints
    """
    def get(self):
        """
        Return code to identify status of the api
        :return response: JSON. Ie, {}
        """
        return "It's working"