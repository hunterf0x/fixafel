"""This module defines the TrxController class for handling transaction-related HTTP routes."""

import json
from typing import Any

from flask import Blueprint, request, Response

from infrastructure.http.contracts.get_transactions_request_contract import GetTransactionsRequestContract
from infrastructure.http.validator.request_validator import validate_request_body
from infrastructure.http.base_controller import BaseController
from application.application_response import ApplicationResponse
from application.use_cases.get_list_transactions.get_list_transactions import GetListTransactionsUseCase
from application.use_cases.get_list_transactions.get_list_transactions_command import GetListTransactionsCommand
from application.use_cases.get_transaction.get_transaction import GetTransactionUseCase
from application.use_cases.get_transaction.get_transaction_command import GetTransactionCommand
from domain.trx_not_found_error import TrxNotFoundError


class TrxController(BaseController):
    """Controller for handling transaction-related HTTP routes."""

    def __init__(self, get_transaction: GetTransactionUseCase, get_list_transactions: GetListTransactionsUseCase):
        """Initialize the TrxController with the given use cases.

        Args:
            get_transaction (GetTransactionUseCase): Use case for getting a single transaction.
            get_list_transactions (GetListTransactionsUseCase): Use case for getting a list of transactions.
        """
        self.__routes = None
        self.register_routes()
        self.__get_transaction = get_transaction
        self.__get_list_transactions = get_list_transactions

    @validate_request_body(request, request_contract=GetTransactionsRequestContract)
    def get_trxs_route(self):
        """Handle the route for getting a list of transactions.

        Returns:
            Response: A Flask response object with the list of transactions.
        """
        body = request.get_json()
        try:
            command = GetListTransactionsCommand(body['list'])
            response: ApplicationResponse = self.__get_list_transactions.execute(command)
            return Response(response=json.dumps(response.to_json()), status=200, mimetype='application/json')
        except Exception as e:
            if isinstance(e, TrxNotFoundError):
                print(e)
                return Response(response=json.dumps({'message': e.args[0]}), status=404, mimetype='application/json')
            raise e

    def get_trx_route(self, trx_id: str):
        """Handle the route for getting a single transaction.

        Args:
            trx_id (str): The ID of the transaction to retrieve.

        Returns:
            Response: A Flask response object with the transaction details.
        """
        try:
            attribute = request.args.get('attribute') or 'TrxNro'
            command = GetTransactionCommand(trx_id, attribute)
            response: ApplicationResponse = self.__get_transaction.execute(command)
            return Response(response=json.dumps(response.to_json()), status=200, mimetype='application/json')
        except Exception as e:
            if isinstance(e, TrxNotFoundError):
                return Response(response=json.dumps({'message': e.args[0]}), status=404, mimetype='application/json')
            raise e

    def register_routes(self):
        """Register the routes for the TrxController."""
        self.__routes = Blueprint('trx_controller', __name__)
        self.__routes.add_url_rule('/<trx_id>', 'get_trx_route', self.get_trx_route, methods=['GET'])
        self.__routes.add_url_rule('', 'get_trxs_route', self.get_trxs_route, methods=['POST'])

    def routes(self) -> Any:
        """Return the routes for the TrxController.

        Returns:
            Any: The routes for the TrxController.
        """
        return self.__routes
