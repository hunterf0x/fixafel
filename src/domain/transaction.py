"""This module defines the Transaction class for handling transaction entities."""

from domain.core.domain_entity import DomainEntity

class Transaction(DomainEntity):
    """Represents a transaction entity."""
    # pylint: disable=too-many-instance-attributes, too-many-arguments
    def __init__(self, doc_id: str, transaction_id: str, trx_nro: str, pk_store: str, pk_terminal: str,
                 pk_transaction_no: int, body: dict, trx_rcp: str, status: str, trx_doc_type: str,
                 note: str):
        super().__init__()
        self.doc_id = doc_id
        self.transaction_id = transaction_id
        self.trx_nro = trx_nro
        self.pk_store = pk_store
        self.pk_terminal = pk_terminal
        self.pk_transaction_no = pk_transaction_no
        self.body = body
        self.trx_rcp = trx_rcp
        self.status = status
        self.trx_doc_type = trx_doc_type
        self.note = note


    @classmethod
    def build(cls, doc_id: str, transaction_id: str, trx_nro: str, pk_store: str, pk_terminal: str,
              pk_transaction_no: int, body: dict, trx_rcp: str, status: str, trx_doc_type: str,
              note: str) -> 'Transaction':
        """Builds a Transaction instance.

        Args:
            doc_id (str): Document ID.
            transaction_id (str): Transaction ID
            trx_nro (str): Transaction number.
            pk_store (str): Store primary key.
            pk_terminal (str): Terminal primary key.
            pk_transaction_no (int): Transaction number primary key.
            body (dict): Transaction body.
            trx_rcp (str): Transaction receipt.
            status (str): Transaction status.
            trx_doc_type (str): Transaction document type.
            note (str): Transaction note.

        Returns:
            Transaction: A new Transaction instance.
        """
        return cls(
            doc_id,
            transaction_id,
            trx_nro,
            pk_store,
            pk_terminal,
            pk_transaction_no,
            body,
            trx_rcp,
            status,
            trx_doc_type,
            note
        )

    def __eq__(self, other: 'Transaction') -> bool:
        """Checks equality between two Transaction instances.

        Args:
            other (Transaction): Another Transaction instance.

        Returns:
            bool: True if both instances are equal, False otherwise.
        """
        if isinstance(other, Transaction):
            return self.trx_nro == other.trx_nro
        return False
