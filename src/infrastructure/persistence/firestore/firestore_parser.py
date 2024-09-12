from src.domain.transaction import Transaction
from src.infrastructure.persistence.database_parser import DatabaseParser


class FirestoreParser(DatabaseParser):
    def to_domain_object(self, database_object: dict) -> Transaction:
        print(f"database: {database_object}")
        return Transaction.build(
            database_object['TrxNro'],
            database_object['PK_Store'],
            database_object['PK_Terminal'],
            database_object['PK_TransactionNo'],
            database_object['body'],
            database_object['trxRcp'],
            database_object['status'],
            database_object['trxDocType']
        )


    def to_database_object(self, domain: Transaction) -> dict:
        return {
            'TrxNro': domain.trxNro,
            'PK_Store': domain.pk_store,
            'PK_Terminal': domain.pk_terminal,
            'PK_TransactionNo': domain.pk_transaction_no,
            'body': domain.body
        }