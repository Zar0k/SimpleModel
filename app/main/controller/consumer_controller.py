from flask import request, Response
from flask import current_app as app
from flask_restplus import Resource, Namespace, fields
from app.main.service.operator_service import get_tour


api = Namespace('consumer', description='kafka consumer')

@api.route('')
class consumer(Resource):
    def get(self):
        """kafka consumer"""
        return get_tour()

