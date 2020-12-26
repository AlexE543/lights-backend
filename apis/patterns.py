from flask import request
from flask_restx import Resource, Namespace
from apis.shared import light_strand
import time
import json

patterns_ns = Namespace("patterns", description="led patterns")


@patterns_ns.route('/hello')
class Hello(Resource):
    def get(self):
        return "Hello!"


@patterns_ns.route('/set_alternating')
@patterns_ns.doc(params={
    'color_one': 'color one',
    'color_two': 'color two'
})
class Hello(Resource):
    def post(self):
        data = json.loads(request.data)
        color_one = data.get('color_one')
        color_two = data.get('color_two')
        print(color_one)
        print(type(color_one))
        return "Hello!"


@patterns_ns.route('/start_alternating')
class Hello(Resource):
    def get(self):
        return "Hello!"
