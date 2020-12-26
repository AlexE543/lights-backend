from flask import Flask, request
from flask_restx import Api, Resource
from light_strand import LightStrand
import time
import board
import neopixel

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class Hello(Resource):
    def get(self):
        return "Hello!"


@api.route('/clear')
class Clear(Resource):
    def get(self):
        start = time.time()
        light_strand.clear()
        end = time.time()
        return f"This command took {end-start} seconds"

@api.route('/fill')
@api.doc(params={
    'r': "red color out of 255",
    'g': "green color out of 255",
    'b': "blue color out of 255",
})
class Fill(Resource):
    def post(self):
        start = time.time()
        r, g, b = request.args.get('r'), request.args.get('g'), request.args.get('b')
        light_strand.fill((r, g, b))
        end = time.time()
        return f"Filling with ({r}, {g}, {b}) took {end-start} seconds"


if __name__ == "__main__":
    light_strand = LightStrand(144, .2)
    app.run()
