from flask import Flask, render_template

from dotenv import load_dotenv
import os

load_dotenv()


def create_app():
    app = Flask(__name__)

    from . public import public_bp
    app.register_blueprint(public_bp)

    return app
