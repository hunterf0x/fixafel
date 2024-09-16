"""This module initializes and runs the Flask application."""

from flask import Flask
from dotenv import load_dotenv
from src.infrastructure.config.config import Config
from src.infrastructure.http.error_handler import handle_exception
from src.container import Container

load_dotenv()

def create_app():
    """Creates and configures the Flask application.

    Returns:
        Flask: The configured Flask application.
    """
    main = Flask(__name__)

    main.register_blueprint(Container.trx_controller().routes(), url_prefix='/trx')
    main.register_error_handler(Exception, handle_exception)

    main.debug = True
    return main

if __name__ == '__main__':
    app = create_app()
    app.run(host=Config.APP_HOST, port=Config.APP_PORT)
