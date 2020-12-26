from flask import request
from flask_restx import Resource, Namespace
from utils.shared import light_strand
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
class SetAlternating(Resource):
    def post(self):
        start = time.time()
        data = json.loads(request.data)
        color_one = tuple(data.get('color_one'))
        color_two = tuple(data.get('color_two'))
        light_strand.set_alternating(color_one, color_two)
        end = time.time()
        return f"Setting alternating colors took {end-start} seconds"


@patterns_ns.route('/start_alternating')
class StartAlternating(Resource):
    def post(self):
        start = time.time()
        data = json.loads(request.data)
        color_one = tuple(data.get('color_one'))
        color_two = tuple(data.get('color_two'))
        light_strand.start_alternating(color_one, color_two)
        end = time.time()
        return f"Starting to alternate colors took {end - start} seconds"


@patterns_ns.route('/set__tri_alternating')
@patterns_ns.doc(params={
    'color_one': 'color one',
    'color_two': 'color two',
    'color_three': 'color_three'
})
class SetTriAlternating(Resource):
    def post(self):
        start = time.time()
        data = json.loads(request.data)
        color_one = tuple(data.get('color_one'))
        color_two = tuple(data.get('color_two'))
        color_three = tuple(data.get('color_three'))
        light_strand.set_alternating(color_one, color_two, color_three)
        end = time.time()
        return f"Setting tri-alternating colors took {end-start} seconds"


@patterns_ns.route('/start_tri_alternating')
class StartTriAlternating(Resource):
    def post(self):
        start = time.time()
        data = json.loads(request.data)
        color_one = tuple(data.get('color_one'))
        color_two = tuple(data.get('color_two'))
        color_three = tuple(data.get('color_three'))
        light_strand.start_alternating(color_one, color_two, color_three)
        end = time.time()
        return f"Starting to tri-alternate colors took {end - start} seconds"


@patterns_ns.route('/stop_playing')
class StopPlaying(Resource):
    def post(self):
        start = time.time()
        light_strand.stop_playing()
        end = time.time()
        return f"Stopping the animation took {end - start} seconds"
