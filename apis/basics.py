from flask import request
from flask_restx import Resource, Namespace
from utils.shared import light_strand
import time
import json

basics_ns = Namespace("basics", description="basic led control")


@basics_ns.route('/hello')
class Hello(Resource):
    def get(self):
        return "Hello!"


@basics_ns.route('/clear')
class Clear(Resource):
    def get(self):
        start = time.time()
        print(light_strand.pixels)
        light_strand.clear()
        end = time.time()
        return f"This command took {end-start} seconds"


@basics_ns.route('/fill')
@basics_ns.doc(params={
    'color': "list of [r, g, b]"
})
class Fill(Resource):
    def post(self):
        start = time.time()
        data = json.loads(request.data)
        color = tuple(data.get('color'))
        light_strand.fill(color)
        end = time.time()
        return f"Filling with {color} took {end-start} seconds"


@basics_ns.route('/fill_range')
@basics_ns.doc(params={
    'color': "list of [r, g, b]",
    'start': "start index",
    'end': "end index"
})
class FillRange(Resource):
    def post(self):
        start = time.time()
        data = json.loads(request.data)
        color = tuple(data.get('color'))
        start_index, end_index = int(data.get('start')), int(data.get('end'))
        light_strand.fill_range(start_index, end_index, color)
        end = time.time()
        return f"Filling the range took {end-start} seconds"


@basics_ns.route('/set_pixel')
@basics_ns.doc(params={
    'color': "list of [r, g, b]",
    'index': "start index",
})
class SetPixel(Resource):
    def post(self):
        start = time.time()
        data = json.loads(request.data)
        color = tuple(data.get('color'))
        idx = int(data.get('index'))
        light_strand.set_pixel(idx, color)
        end = time.time()
        return f"Setting the pixel took {end-start} seconds"


@basics_ns.route('/get_pixel')
@basics_ns.doc(params={
    'index': "start index",
})
class SetPixel(Resource):
    def get(self):
        start = time.time()
        data = json.loads(request.data)
        idx = int(data.get('index'))
        color = light_strand.get_pixel(idx)
        end = time.time()
        return f"The color of pixel {idx} is {color}. Getting the pixel took {end-start} seconds"

