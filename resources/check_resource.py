from flask_restful import Resource
from controllers.template_database_controller import TemplateDatabaserController

class CheckResource(Resource):
    """
    Check API Endpoints
    """
    def get(self):
        """
        Return code to identify status of the api
        :return response: JSON. Ie, {}
        """
        return TemplateDatabaserController.check_template_database()