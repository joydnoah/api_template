# Python packages
from os import path

# External packages
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

# Local packages
from config import TEMPLATE_DATABASE_URI

app = Flask(__name__)
CORS(app)
load_dotenv(path.join(path.dirname(__file__), '.env'))
app.config.from_object('config')


@app.errorhandler(Exception)
def exception_error(e):
    """
    Return default 500 code when an unhandled exception is raised.
    :param e: Exception instance.
    :return: Response instance.
    """
    return jsonify({'message': 'There was an unexpected error'}), 500

db = SQLAlchemy(app)
db.app = app
db.init_app(app)

template_database_connection = create_engine(TEMPLATE_DATABASE_URI, echo=False)