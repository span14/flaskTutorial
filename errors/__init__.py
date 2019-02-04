from flask import Blueprint

bp = Blueprint('errors', __name__)

from flaskTutorial.errors import handlers