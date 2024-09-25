"""This module configures logging for the application."""

import sys
import os
import logging
from colorlog import ColoredFormatter
from infrastructure.logger.logger_formatter import CustomJsonFormatter

def configure_logging():
    """Configures the logging settings based on the environment."""
    date_format = "%Y-%m-%d %H:%M:%S"
    env = os.getenv('ENV', 'development')

    if env == 'production':
        log_format = '%(asctime)s %(levelname)s %(name)s %(funcName)s %(message)s'
        formatter = CustomJsonFormatter(
            fmt=log_format,
            rename_fields={
                "asctime": "dateTime", 'levelname': 'level', 'funcName': 'function', 'name': 'logger', "message": "msg"
            },
            datefmt=date_format
        )
    else:
        log_format = "%(asctime)s [%(log_color)s%(levelname)s%(reset)s] - %(funcName)s - %(name)s - %(message)s"
        formatter = ColoredFormatter(
            log_format,
            datefmt=date_format,
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red'
            }
        )

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    logging.basicConfig(level=logging.DEBUG, handlers=[handler], encoding='utf-8')

def get_logger(name: str = 'DefaultLogger') -> logging.Logger:
    """Gets a logger instance with the specified name.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: The logger instance.
    """
    logger = logging.getLogger(name)
    return logger
