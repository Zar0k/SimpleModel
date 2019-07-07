from flask_restplus import Api, Namespace
from flask import Blueprint

from .main.controller.health_controller import api as health_namespace
from .main.controller.operator_controller import api as operator_namespace
from .main.controller.consumer_controller import api as consumer_namespace

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='tourmodel',
          version='1.0',
          description='tourmodel service'
          )

api.add_namespace(health_namespace, path='/health')
api.add_namespace(operator_namespace)
api.add_namespace(consumer_namespace, path='/consume')