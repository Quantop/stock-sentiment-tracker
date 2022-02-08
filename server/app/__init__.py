from flask import Flask, jsonify
from flask_cors import CORS

from .extensions import mongo
from .main import main

def create_app(config_object='app.settings'):
  app = Flask(__name__)

  app.config.from_object(config_object)

  # enable CORS
  CORS(app, resources={r'/*': {'origins': '*'}})

  # initializing mongo
  mongo.init_app(app)

  # registering blueprint from main
  app.register_blueprint(main)

  return app