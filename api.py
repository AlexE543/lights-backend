from flask import Flask
from flask_restx import Api, Resource
import time
import board
import neopixel

app = Flask(__name__)
api = Api(app)


@app.route('/hello')
class Hello(Resource):
    def get(self):
        return "Hello!"


if __name__ == "__main__":
    app.run()