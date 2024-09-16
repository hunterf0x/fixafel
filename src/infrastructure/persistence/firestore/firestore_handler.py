"""This module defines the FirestoreHandler class for handling Firestore database operations."""

from typing import Any
from google.cloud import firestore
from google.oauth2 import service_account
from src.infrastructure.config.config import Config
from src.infrastructure.persistence.database_handler import DatabaseHandler

# pylint: disable=too-few-public-methods
class FirestoreHandler(DatabaseHandler):
    """Class for handling Firestore database operations."""

    def __init__(self, config: Config):
        """Initialize the FirestoreHandler with the given configuration.

        Args:
            config (Config): The configuration object.
        """
        self.__config = config
        self.__initialize()

    def get_database(self) -> Any:
        """Retrieve the Firestore database instance.

        Returns:
            Any: The Firestore database instance.
        """
        credentials = service_account.Credentials.from_service_account_file(
            self.__config.GOOGLE_APPLICATION_CREDENTIALS
        )
        return firestore.Client(
            project=self.__config.GCLOUD_PROJECT,
            credentials=credentials,
            database=self.__config.DB_NAME
        )

    def __initialize(self) -> None:
        """Initialize the Firestore database."""
        self.get_database()
