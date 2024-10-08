"""This module defines the FirestoreRepository class for handling Firestore database operations."""

import logging
from types import NoneType
from typing import Optional

from google.cloud.exceptions import GoogleCloudError
from google.cloud.firestore_v1 import FieldFilter

from domain.trx_repository import TrxRepository
from domain.transaction import Transaction
from infrastructure.persistence.database_handler import DatabaseHandler
from infrastructure.persistence.database_parser import DatabaseParser


class FirestoreRepository(TrxRepository):
    """Class for handling Firestore database operations."""

    def __init__(self, database_handler: DatabaseHandler, database_parser: DatabaseParser, logger: logging.Logger):
        """Initialize the FirestoreRepository with the given database handler and parser.

        Args:
            database_handler (DatabaseHandler): The database handler instance.
            database_parser (DatabaseParser): The database parser instance.
        """
        self.__db = database_handler.get_database()
        self.__trx_parser: DatabaseParser = database_parser
        self.logger = logger

    @staticmethod
    def chunk_list(data, chunk_size):
        """Chunk a list into smaller lists of a specified size.

        Args:
            data (list): The list to chunk.
            chunk_size (int): The size of each chunk.

        Returns:
            list: A list of chunked lists.
        """
        return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    def find_one(self, transaction_param: str, attr: str) -> Optional[Transaction]:
        """Find a single transaction by attribute.

        Args:
            transaction_param (str): The transaction param to search for.
            attr (str): The attribute to search by.

        Returns:
            Optional[Transaction]: The found transaction or None if not found.
        """
        data: dict = {}
        try:
            documents = self.__db.collection('salesTrxCo').where(
                filter=FieldFilter(attr, '==', transaction_param)).limit(1).get()

            if not documents:
                return None

            for doc in documents:
                data = doc.to_dict()
                data['doc_id'] = doc.id
                print(f"doc: {doc}")
                print(f"Datos del documento: {data.get('TrxNro')}")
                print(f"Datos del documento: {data}")
        except GoogleCloudError as e:
            self.logger.error("Error when searching for transaction: %s", e)
        except Exception  as e:
            self.logger.exception("Error when searching for transaction: %s", e, exc_info=True)

        return None if isinstance(data, NoneType) else self.__trx_parser.to_domain_object(data)

    def get_list(self, trx_list: list) -> list[Transaction] | None:
        """Get a list of transactions by their IDs.

        Args:
            trx_list (list): The list of transaction IDs to search for.

        Returns:
            list[Transaction] | None: The list of found transactions or None if none found.
        """
        transactions: list = []
        print(trx_list)
        print("Get list")

        chunked_list = self.chunk_list(trx_list, 10)

        for chunk in chunked_list:
            try:
                documents = self.__db.collection('salesTrxCo').where(filter=FieldFilter('TrxNro', 'in', chunk)).get()
                print(f"Documentos encontrados: {documents}")

                if not documents:
                    return None

                for doc in documents:
                    data = doc.to_dict()
                    data['doc_id'] = doc.id
                    transactions.append(self.__trx_parser.to_domain_object(data))
            except GoogleCloudError as e:
                self.logger.error("Error when searching for transaction: %s", e)
            except Exception as e:
                self.logger.exception("Error when searching for transaction: %s", e, exc_info=True)

        return None if not transactions else transactions

    def update(self, doc_id, attributes) -> Transaction | None:
        """Update a transaction document with new attributes.

        Args:
            doc_id (str): The ID of the document to update.
            attributes (dict): The attributes to update in the document.

        Returns:
            Transaction | None: The updated transaction or None if the document does not exist.
        """
        doc_ref = self.__db.collection('salesTrxCo').document(doc_id)
        transaction = None
        try:
            if not doc_ref.get().exists:
                print(f"El documento con ID {doc_id} no existe.")
                return None
            doc_ref.update(attributes)
            transaction = doc_ref.get().to_dict()
            transaction['doc_id'] = doc_ref.id
            self.logger.info(f"Transaction {doc_id} has been updated.")
        except GoogleCloudError as e:
            self.logger.error("Error when updating transaction: %s", e)
        except Exception as e:
            self.logger.exception("Error when updating transaction: %s", e, exc_info=True)

        return None if isinstance(transaction, NoneType) else self.__trx_parser.to_domain_object(transaction)
