from app import app
from api import set_up_api
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)
set_up_api(app)

if __name__ == "__main__":
    manager.run()