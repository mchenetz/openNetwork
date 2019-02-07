from flask import Flask
from flask_restful import Api, Resource, reqparse
import openNetwork
record = openNetwork.populateYamlDef()


app = Flask(__name__)
api = Api(app)

class Auth(Resource):
    def get(self, name):
        pass
    def post(self, name, request=None):
        pass
    def put(self, name, request=None):
        pass
    def put(self, name):
        pass

class Device(Resource):
    def get(self, name):
        pass
    def post(self, name,):
        pass
    def put(self, name):
        pass
    def delete(self, name):
        pass

class API(Resource):
    def get(self, name):
        for rec in record:
            if name == rec['name']:
                return rec['cmd']
    def post(self, name, request=None):
        pass
    def put(self, name, request=None):
        pass
    def delete(self, name):
        pass

api.add_resource(Device, "/api/device/<string:name>")
api.add_resource(API, "/api/cmd/<string:name>")
app.run(debug=True)