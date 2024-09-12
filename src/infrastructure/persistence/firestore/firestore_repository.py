from types import NoneType
from typing import Optional

from google.cloud.firestore_v1 import FieldFilter

from src.domain.trx_repository import TrxRepository
from src.domain.transaction import Transaction
from src.infrastructure.persistence.database_handler import DatabaseHandler
from src.infrastructure.persistence.database_parser import DatabaseParser


class FirestoreRepository(TrxRepository):
    def __init__(self, database_handler: DatabaseHandler, database_parser: DatabaseParser):
        self.__db = database_handler.get_database()
        self.__trx_parser: DatabaseParser = database_parser

    def find_one(self, id: str, attr: str) -> Optional[Transaction]:
        data: dict = dict()
        print(attr)
        try:
            documents = self.__db.collection('salesTrxCo').where(filter=FieldFilter(attr, '==', id)).limit(1).get()
            print(f"Documentos encontrados: {documents}")

            if not documents:
                return None

            for doc in documents:
                data = doc.to_dict()
                print(f"Datos del documento: {data}")
        except Exception as e:
            print(f"Error al buscar la transacción: {e}")

        #return None
        return None if isinstance(data, NoneType) else self.__trx_parser.to_domain_object(data)
