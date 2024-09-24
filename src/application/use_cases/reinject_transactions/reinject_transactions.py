"""This module defines the use case for reinjecting transactions."""

import json
from application.application_service import ApplicationService
from application.use_cases.reinject_transactions.reinject_transactions_command import ReinjectTransactionsCommand
from application.use_cases.reinject_transactions.reinject_transactions_response import ReinjectedTransactionsResponse
from domain.trx_repository import TrxRepository

class ReinjectTransactionsUseCase(ApplicationService):
    """Use case for reinjecting transactions."""

    def __init__(self, transaction_repository: TrxRepository, logger):
        """Initializes the use case with the given transaction repository and logger.

        Args:
            transaction_repository (TrxRepository): The transaction repository instance.
            logger: The logger instance.
        """
        self.transaction_repository = transaction_repository
        self.logger = logger

    def execute(self, command: ReinjectTransactionsCommand) -> ReinjectedTransactionsResponse:
        """Executes the reinjection of transactions.

        Args:
            command (ReinjectTransactionsCommand): The command containing the list of transactions to reinject.

        Returns:
            ReinjectedTransactionsResponse: The response containing the result of the reinjection.
        """
        transactions = command.transaction_list
        print(transactions)
        result = []

        for transaction in transactions:
            print(transaction.get('doc_id'))
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
                'status': 'APPROVED',
                'note': 'TRXs Pending requested by GIK-17604'
            }

            if sale_updated or payment_updated:
                fields_to_update['body'] = json.dumps(body)

            result.append(self.transaction_repository.update(transaction.get('doc_id'), fields_to_update))

        return ReinjectedTransactionsResponse(result)

    def log_transaction(self, transaction_id: str):
        """Logs the transaction ID.

        Args:
            transaction_id (str): The ID of the transaction to log.
        """
        self.logger.info(f"Transaction {transaction_id} has been processed.")
