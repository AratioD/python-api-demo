from flask import Flask
from flask_restful import Resource, Api
from io import StringIO
import json
import requests
# import urllib.request, json

app = Flask(__name__)
api = Api(app)



url = 'https://raw.githubusercontent.com/solita/dev-academy-2021/main/names.json'
resp = requests.get(url)
data = json.loads(resp.text)
print(data)



collegians = []


class Names(Resource):
    def get(self, name):
        for colleg_name in collegians:
            if colleg_name['name'] == name:
                return colleg_name
        return {'name': none}, 404

        return {'student': name}

    def post(self, name):
        colleg_name = {'name': name, 'price': 12.00}
        collegians.append(colleg_name)
        return colleg_name


api.add_resource(Names, '/names/<string:name>')

app.run(port=5000)
