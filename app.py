"""This module initializes and runs the Flask application."""

from flask import Flask
from dotenv import load_dotenv
from infrastructure.config.config import Config
from infrastructure.http.error_handler import handle_exception
from infrastructure.logger.logger_config import configure_logging, get_logger
from container import Container


load_dotenv()

configure_logging()

logger = get_logger(__name__)

def create_app() -> Flask:
    """Creates and configures the Flask application.

    Returns:
        Flask: The configured Flask application.
    """
    main = Flask(__name__)

    main.register_blueprint(Container.trx_controller().routes(), url_prefix='/transactions')
    main.register_error_handler(Exception, handle_exception)

    main.debug = Config.DEBUG

    logger.info("Flask application created successfully.")
    return main

if __name__ == '__main__':
    app = create_app()

    host = Config.APP_HOST
    port = Config.APP_PORT

    app.run(host=host, port=port)