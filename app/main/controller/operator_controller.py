import json
import xmltodict
from flask import request, Response
from flask import current_app as app
from flask_restplus import Resource, Namespace, fields
from app.main.service.operator_service import save_tours


api = Namespace('operators', description='operators api simulated')

@api.route('/json')
class OperatorJson(Resource):
    """
        json operator resource
    """
    def get(self):
        file = open('doc/json/operator.json')
        data = json.load(file)
        return save_tours(data)

@api.route('/xml')
class OperatorXml(Resource):
    """
        xml operator resource
    """
    def get(self):
        with open("doc/xml/operator.xml", 'r') as f:
            xmlString = f.read()            
        json_string = json.dumps(xmltodict.parse(xmlString), indent=4)
        data = json.loads(json_string)
        return save_tours(data['data']['tour'])