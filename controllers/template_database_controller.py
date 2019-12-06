from managers.template_database_manager import TemplateDatabaserManager

class TemplateDatabaserController(object):
    @staticmethod
    def check_template_database():
        """
        Ping template database to test the connection
        :return Return a 'It's working' if the connection is fine, or 'There was an error while connecting to the db' if there was an error while connection to the db
        """
        if TemplateDatabaserManager.check_template_database():
            return "It's working"
        else:
            return 'There was an error while connecting to the db'
