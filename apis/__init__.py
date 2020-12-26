from flask import Flask
from flask_restx import Api
from apis.light_strand import LightStrand
from .basics import basics_ns
from .patterns import patterns_ns


def create_app():
    global light_strand
    light_strand = LightStrand(144, brightness=0.2)

    app = Flask(__name__)

    api = Api(
        title="lights-backend",
        version='0.1.0',
        description="light controller apis"
    )
    api.add_namespace(basics_ns)
    api.add_namespace(patterns_ns)
    api.init_app(app)
    return app, api
