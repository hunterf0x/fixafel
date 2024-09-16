"""Transactions controller."""
import json
from typing import Any


from flask import Blueprint, request, Response

from src.application.application_response import ApplicationResponse
from src.application.use_cases.get_list_transactions.get_list_transactions import (
    GetListTransactionsUseCase )
from src.application.use_cases.get_list_transactions.get_list_transactions_command import GetListTransactionsCommand
from src.application.use_cases.get_transaction.get_transaction import GetTransactionUseCase
from src.application.use_cases.get_transaction.get_transaction_command import GetTransactionCommand
from src.domain.trx_not_found_error import TrxNotFoundError
from src.infrastructure.http.base_controller import BaseController


class TrxController(BaseController):
    """Transactions controller."""
    def __init__(self, get_transaction: GetTransactionUseCase, get_list_transactions: GetListTransactionsUseCase):
        self.__routes = None
        self.register_routes()
        self.__get_transaction = get_transaction
        self.__get_list_transactions = get_list_transactions

    def get_trxs_route(self):
        """Get transactions route."""
        body = request.get_json()
        try:
            command = GetListTransactionsCommand(body['list'])
            response: ApplicationResponse = self.__get_list_transactions.execute(command)
            return Response(response=json.dumps(response.to_json()), status=200, mimetype='application/json')
        except Exception as e:
            print(e)
            print("esto es un error")
            if isinstance(e, TrxNotFoundError):
                return Response(response=json.dumps({'message': e.message}), status=404, mimetype='application/json')
            raise e



    def get_trx_route(self, trx_id: str):
        """Get transaction route."""
        try:
            attribute = request.args.get('attribute') or 'TrxNro'
            command = GetTransactionCommand(trx_id, attribute)
            response: ApplicationResponse = self.__get_transaction.execute(command)
            return Response(response=json.dumps(response.to_json()), status=200, mimetype='application/json')
        except Exception as e:
            print(e)
            if isinstance(e, TrxNotFoundError):
                return Response(response=json.dumps({'message': e.message}), status=404, mimetype='application/json')
            raise e

    def register_routes(self):
        """Register routes."""
        self.__routes = Blueprint('trx_controller', __name__)
        self.__routes.add_url_rule('/<trx_id>', 'get_trx_route', self.get_trx_route, methods=['GET'])
        self.__routes.add_url_rule('', 'get_trxs_route', self.get_trxs_route, methods=['POST'])

    def routes(self) -> Any:
        """Get routes."""
        return self.__routes
