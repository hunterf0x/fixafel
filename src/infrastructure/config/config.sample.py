import os

class Config(object):
    APP_PORT = os.getenv('APP_PORT') or 5001
    APP_HOST = os.getenv('APP_HOST') or '127.0.0.1'
    FIRESTORE_CREDENTIALS = os.getenv('FIRESTORE_CREDENTIALS')
    GCLOUD_PROJECT = os.getenv('GCLOUD_PROJECT')
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

class RunConfig(Config):
    DB_NAME = os.getenv('DB_NAME') or 'acl-db'

app_config = {
    'run': RunConfig
}
