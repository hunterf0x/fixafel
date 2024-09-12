from flask import Flask, render_template

from dotenv import load_dotenv
import os




load_dotenv()

from google.oauth2 import service_account
from google.cloud import firestore
from datetime import datetime
from tabulate import tabulate
from pathlib import Path
from IPython.display import display, HTML
import pandas as pd
import zipfile
import base64
import json
import time
import os

GCLOUD_PROJECT = os.environ.get('GCLOUD_PROJECT')
FIRESTORE_CREDENTIALS = os.environ.get('FIRESTORE_CREDENTIALS')


creds = json.loads( base64.b64decode(FIRESTORE_CREDENTIALS).decode('utf-8'))
credentials = service_account.Credentials.from_service_account_info(creds)

scoped_credentials = credentials.with_scopes(
    ['https://www.googleapis.com/auth/cloud-platform'])

db = firestore.Client(project=GCLOUD_PROJECT, credentials=credentials)





#@app.route('/')
#def index():
   # return render_template('index.html')


from src.infrastructure.config.config import Config
from src.container import Container


def create_app():
    main = Flask(__name__)

    main.register_blueprint(Container.trx_controller().routes(), url_prefix='/trx')

    main.debug = True
    return main


if __name__ == '__main__':
    app = create_app()
    app.run(host=Config.APP_HOST, port=Config.APP_PORT)
