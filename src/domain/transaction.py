"""This module defines the Transaction class for handling transaction entities."""

from domain.core.domain_entity import DomainEntity

class Transaction(DomainEntity):
    """Represents a transaction entity."""
    # pylint: disable=too-many-instance-attributes, too-many-arguments
    def __init__(self, trx_nro: str, pk_store: str, pk_terminal: str, pk_transaction_no: int,
                 body: dict, trx_rcp: str, status: str, trx_doc_type: str):
        super().__init__()
        self.trxNro = trx_nro
        self.pk_store = pk_store
        self.pk_terminal = pk_terminal
        self.pk_transaction_no = pk_transaction_no
        self.body = body
        self.trxRcp = trx_rcp
        self.status = status
        self.trxDocType = trx_doc_type

    @classmethod
    def build(cls, trx_nro: str, pk_store: str, pk_terminal: str, pk_transaction_no: int,
              body: dict, trx_rcp: str, status: str, trx_doc_type: str) -> 'Transaction':
        """Builds a Transaction instance.

        Args:
            trx_nro (str): Transaction number.
            pk_store (str): Store primary key.
            pk_terminal (str): Terminal primary key.
            pk_transaction_no (int): Transaction number primary key.
            body (dict): Transaction body.
            trx_rcp (str): Transaction receipt.
            status (str): Transaction status.
            trx_doc_type (str): Transaction document type.

        Returns:
            Transaction: A new Transaction instance.
        """
        return cls(trx_nro, pk_store, pk_terminal, pk_transaction_no, body, trx_rcp, status, trx_doc_type)

    def __eq__(self, other: 'Transaction') -> bool:
        """Checks equality between two Transaction instances.

        Args:
            other (Transaction): Another Transaction instance.

        Returns:
            bool: True if both instances are equal, False otherwise.
        """
        if isinstance(other, Transaction):
            return self.trxNro == other.trxNro
        return False
