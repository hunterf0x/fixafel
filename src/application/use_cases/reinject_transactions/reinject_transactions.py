import json

from application.application_service import ApplicationService
from application.use_cases.reinject_transactions.reinject_transactions_command import ReinjectTransactionsCommand
from application.use_cases.reinject_transactions.reinject_transactions_response import ReinjectedTransactionsResponse
from domain.trx_repository import TrxRepository


class ReinjectTransactionsUseCase(ApplicationService):
    def __init__(self, transaction_repository: TrxRepository):
        self.transaction_repository = transaction_repository

    def execute(self, command: ReinjectTransactionsCommand) -> ReinjectedTransactionsResponse:
        transactions = command.transaction_list
        result = []

        for transaction in transactions:

            fields_to_update = {}
            sale_updated = False
            payment_updated = False
            body = json.loads(transaction.get('body'))

            payments = body.get('ACL_Trx_Payments')
            sales = body.get('ACL_Trx_Sales')

            for sale in sales:
                if 'saleClaCom' not in sale:
                    sale['saleClaCom'] = ""

                if sale['saleClaCom'] == "":
                    sale_updated = True

            for payment in payments:
                if 'payIDPoints' not in payment:
                    payment['payIDPoints'] = ""
                    payment_updated = True

            fields_to_update = {
                'status': 'PENDING',
                'notes': 'Reinjecting transaction'
            }

            if sale_updated or payment_updated:
                fields_to_update['body'] = json.dumps(body)

            result.append(self.transaction_repository.update(transaction.doc_id, fields_to_update))

        return ReinjectedTransactionsResponse(result)