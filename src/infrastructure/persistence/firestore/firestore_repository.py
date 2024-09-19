"""This module defines the FirestoreRepository class for handling Firestore database operations."""

from types import NoneType
from typing import Optional

from google.cloud.firestore_v1 import FieldFilter

from domain.trx_repository import TrxRepository
from domain.transaction import Transaction
from infrastructure.persistence.database_handler import DatabaseHandler
from infrastructure.persistence.database_parser import DatabaseParser


class FirestoreRepository(TrxRepository):
    """Class for handling Firestore database operations."""

    def __init__(self, database_handler: DatabaseHandler, database_parser: DatabaseParser):
        """Initialize the FirestoreRepository with the given database handler and parser.

        Args:
            database_handler (DatabaseHandler): The database handler instance.
            database_parser (DatabaseParser): The database parser instance.
        """
        self.__db = database_handler.get_database()
        self.__trx_parser: DatabaseParser = database_parser

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

    def find_one(self, trx_id: str, attr: str) -> Optional[Transaction]:
        """Find a single transaction by attribute.

        Args:
            trx_id (str): The transaction ID to search for.
            attr (str): The attribute to search by.

        Returns:
            Optional[Transaction]: The found transaction or None if not found.
        """
        data: dict = {}
        try:
            documents = self.__db.collection('salesTrxCo').where(filter=FieldFilter(attr, '==', trx_id)).limit(1).get()
            print(f"Documentos encontrados: {documents}")

            if not documents:
                return None

            for doc in documents:
                data = doc.to_dict()
                print(f"Datos del documento: {data}")
        except Exception  as e:
            print(f"Error al buscar la transacción: {e}")

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
                    transactions.append(self.__trx_parser.to_domain_object(data))
            except Exception as e:
                print(f"Error al buscar la transacción: {e}")

        print(f"Transacciones encontradas: {transactions}")

        return None if not transactions else transactions
