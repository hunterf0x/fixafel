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

    @staticmethod
    def chunk_list(data, chunk_size):
        return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

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

    def get_list(self, trx_list: list) -> list[Transaction] | None:
        transactions: list = list()
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
                    #print(f"Datos del documento: {data}")
                    transactions.append(self.__trx_parser.to_domain_object(data))
            except Exception as e:
                print(f"Error al buscar la transacción: {e}")

        print(f"Transacciones encontradas: {transactions}")

        return None if not transactions else transactions
