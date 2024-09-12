import os
import base64
import json
from typing import Any
from google.cloud import firestore
from google.oauth2 import service_account
from src.infrastructure.config.config import Config
from src.infrastructure.persistence.database_handler import DatabaseHandler


class FirestoreHandler(DatabaseHandler):
    def __init__(self, config: Config):
        self.__config = config
        self.__initialize()

    def get_database(self) -> Any:
        #creds = json.loads(base64.b64decode(self.__config.FIRESTORE_CREDENTIALS).decode('utf-8'))
        credentials = service_account.Credentials.from_service_account_file(self.__config.GOOGLE_APPLICATION_CREDENTIALS)
        #scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])
        return firestore.Client(project=self.__config.GCLOUD_PROJECT, credentials=credentials, database=self.__config.DB_NAME)

    def __initialize(self) -> None:
        db = self.get_database()
        # Firestore does not require explicit index creation like MongoDB
        # You can define indexes in the Firestore console or via index configuration files