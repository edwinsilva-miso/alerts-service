from flask import Blueprint
from src.ports.input.controllers.alert_controller import alerts

# main blueprint to be registered with application
api = Blueprint('api', __name__)

# register user with api blueprint
api.register_blueprint(alerts, url_prefix="/alerts")