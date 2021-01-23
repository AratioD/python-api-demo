from flask import Flask
from flask_restful import Resource, Api
import json
import requests

app = Flask(__name__)
api = Api(app)


def read_url():
    # Read data from SOLITA GitHub
    url = 'https://raw.githubusercontent.com/solita/dev-academy-2021/main/names.json'
    resp = requests.get(url)
    return json.loads(resp.text)


def process_json():
    keys, values = zip(*read_url().items())
    name_values = zip(*values)

    name_values = list(zip(*name_values))
    name_list = []
    for ii in name_values:
        for dd in ii:
            keys, values = zip(*dd.items())
            name_list.append(values)

    return name_list


# 1. List names and amounts, order by amount, most popular first
class AmountsOrder(Resource):
    def get(self):
        if not process_json():
            return {'Amounts': None}, 404
        else:
            return sorted(process_json(), key=lambda x: (-x[1], x[0]))


# 2. List names in alphabetical order
class NamesOrder(Resource):
    def get(self):
        if not process_json():
            return {'Names': None}, 404
        else:
            return sorted(process_json(), key=lambda x: (x[0], x[0]))


# 3. Return the total amount of all the names
class NamesAmount(Resource):
    def get(self):
        if not process_json():
            return {'Amount': None}, 404
        else:
            return {'Total amount of names -->': len(process_json())}


# 4. Return the amount of the name given as a parameter
class Name(Resource):
    def get(self, name):
        for elem in process_json():
            if elem[0].lower() == name.lower():
                return {'amount': elem[1]}
        return {'amount': None}, 404


# 1. List names and amounts, order by amount, most popular first
api.add_resource(AmountsOrder, '/amounts/')
# 2. List names in alphabetical order
api.add_resource(NamesOrder, '/names/')
# 3. Return the total amount of all the names
api.add_resource(NamesAmount, '/amount/')
# 4. Return the amount of the name given as a parameter
api.add_resource(Name, '/name/<string:name>')

if __name__ == '__main__':
    read_url()
    process_json()
    app.run(port=5000)
