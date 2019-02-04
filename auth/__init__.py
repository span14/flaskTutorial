from flask import Blueprint

# TODO: make name and import_name different for testing
bp = Blueprint('auth', __name__)

from flaskTutorial.auth import routes