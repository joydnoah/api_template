from app import template_database_connection as engine

class TemplateDatabaserManager(object):
    @staticmethod
    def check_template_database():
        """
        Ping template database to test the connection
        :return Return a DB result if the conection is fine, or false if there is an error while connection
        """
        try:
            with engine.contextual_connect(close_with_result=True):
                query = "SELECT 1"
                return engine.execute(query)
        except Exception as e:
            return False