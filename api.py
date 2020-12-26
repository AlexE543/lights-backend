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
        r, g, b = int(request.args.get('r')), int(request.args.get('g')), int(request.args.get('b'))
        light_strand.fill((r, g, b))
        end = time.time()
        return f"Filling with ({r}, {g}, {b}) took {end-start} seconds"


@api.route('/fill_range')
@api.doc(params={
    'r': "red color out of 255",
    'g': "green color out of 255",
    'b': "blue color out of 255",
    'start': "start index",
    'end': "end index"
})
class FillRange(Resource):
    def post(self):
        start = time.time()
        r, g, b = int(request.args.get('r')), int(request.args.get('g')), int(request.args.get('b'))
        start_index, end_index = int(request.args.get('start')), int(request.args.get('end'))
        light_strand.fill_range(start_index, end_index, (r, g, b))
        end = time.time()
        return f"Filling the range took {end-start} seconds"

@api.route('/set_pixel')
@api.doc(params={
    'r': "red color out of 255",
    'g': "green color out of 255",
    'b': "blue color out of 255",
    'index': "start index",
})
class SetPixel(Resource):
    def post(self):
        start = time.time()
        r, g, b = int(request.args.get('r')), int(request.args.get('g')), int(request.args.get('b'))
        idx = int(request.args.get('index'))
        light_strand.set_pixel(idx, (r, g, b))
        end = time.time()
        return f"Setting the pixel took {end-start} seconds"


@api.route('/get_pixel')
@api.doc(params={
    'index': "start index",
})
class SetPixel(Resource):
    def get(self):
        start = time.time()
        idx = int(request.args.get('index'))
        color = light_strand.get_pixel(idx)
        end = time.time()
        return f"The color of pixel {idx} is {color}. Getting the pixel took {end-start} seconds"


if __name__ == "__main__":
    light_strand = LightStrand(144, .2)
    app.run()
