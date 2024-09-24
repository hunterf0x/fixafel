"""This module defines the FirestoreParser class for parsing Firestore database objects."""

from domain.transaction import Transaction
from infrastructure.persistence.database_parser import DatabaseParser

class FirestoreParser(DatabaseParser):
    """Class for parsing Firestore database objects."""

    def to_domain_object(self, database_object: dict) -> Transaction:
        """Convert a Firestore database object to a Transaction domain object.

        Args:
            database_object (dict): The Firestore database object to convert.

        Returns:
            Transaction: The Transaction domain object.
        """
        return Transaction.build(
            database_object['doc_id'],
            database_object['id'],
            database_object['TrxNro'],
            database_object['PK_Store'],
            database_object['PK_Terminal'],
            database_object['PK_TransactionNo'],
            database_object['body'],
            database_object['trxRcp'],
            database_object['status'],
            database_object['trxDocType'],
            database_object.get('note', "")
        )

    def to_database_object(self, domain: Transaction) -> dict:
        """Convert a Transaction domain object to a Firestore database object.

        Args:
            domain (Transaction): The Transaction domain object to convert.

        Returns:
            dict: The Firestore database object.
        """
        return {
            'TrxNro': domain.trxNro,
            'PK_Store': domain.pk_store,
            'PK_Terminal': domain.pk_terminal,
            'PK_TransactionNo': domain.pk_transaction_no,
            'body': domain.body
        }
