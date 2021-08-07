from flask import Blueprint, Flask
from flask_cors import CORS

from jazz.api import api
from jazz.api.healthcheck.view import ns as healthcheck
from jazz.api.bazooka.view import ns as bazooka

def create_app(config_filename=None):
  app = Flask(__name__)
  CORS(app, resources={r"/*": {"origins": "*"}})

  blueprint = Blueprint('jazz', __name__)
  api.init_app(blueprint)
  api.add_namespace(healthcheck, "/healthcheck")
  api.add_namespace(bazooka, "/bazooka")

  app.register_blueprint(blueprint)

  return app
