from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from .basics import basics_ns
from .patterns import patterns_ns
from .spotify import spotify_ns


def create_app():
    app = Flask(__name__)
    CORS(app)
    api = Api(
        title="lights-backend",
        version='0.1.0',
        description="light controller apis"
    )
    api.add_namespace(basics_ns)
    api.add_namespace(patterns_ns)
    api.add_namespace(spotify_ns)
    api.init_app(app)
    return app, api
