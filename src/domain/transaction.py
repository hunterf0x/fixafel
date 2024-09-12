from src.domain.core.domain_entity import DomainEntity

class Transaction(DomainEntity):
    def __init__(self, trx_nro: str, pk_store: str, pk_terminal: str, pk_transaction_no: int, body: dict, trx_rcp: str, status: str, trx_doc_type: str):
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
    def build(cls, trx_nro: str, pk_store: str, pk_terminal: str, pk_transaction_no: int, body: dict, trx_rcp: str, status: str, trx_doc_type: str) -> 'Transaction':
        return cls(trx_nro, pk_store, pk_terminal, pk_transaction_no, body, trx_rcp, status, trx_doc_type)

    def __eq__(self, other: 'Transaction') -> bool:
        if isinstance(other, Transaction):
            return self.trxNro == other.trxNro
        return False