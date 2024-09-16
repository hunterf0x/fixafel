"""This  is a template and defines the configuration classes for the application."""

import os

class Config:
    """Base configuration class."""
    # pylint: disable=too-few-public-methods
    APP_PORT = os.getenv('APP_PORT') or 5001
    APP_HOST = os.getenv('APP_HOST') or '127.0.0.1'
    FIRESTORE_CREDENTIALS = os.getenv('FIRESTORE_CREDENTIALS')
    GCLOUD_PROJECT = os.getenv('GCLOUD_PROJECT')
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

class RunConfig(Config):
    """Run configuration class."""
    # pylint: disable=too-few-public-methods
    DB_NAME = os.getenv('DB_NAME') or 'acl-db'

app_config = {
    'run': RunConfig
}
