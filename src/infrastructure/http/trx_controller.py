import json
from typing import Any

from flask import Blueprint, Response
from flask import request

from src.application.application_response import ApplicationResponse
from src.application.use_cases.get_transaction.get_transaction import GetTransactionUseCase
from src.application.use_cases.get_transaction.get_transaction_command import GetTransactionCommand
from src.domain.trx_not_found_error import TrxNotFoundError
from src.infrastructure.http.base_controller import BaseController


class TrxController(BaseController):
    def __init__(self, get_transaction: GetTransactionUseCase):
        self.__routes = None
        self.register_routes()
        self.__trx_service = get_transaction

    def test(self):
        return 'Hello World'

    def get_trx_route(self, trx_id: str):
        try:
            attribute = request.args.get('attribute') or 'TrxNro'
            command = GetTransactionCommand(trx_id, attribute)
            response: ApplicationResponse = self.__trx_service.execute(command)
            return Response(response=json.dumps(response.to_json()), status=200, mimetype='application/json')
        except Exception as e:
            print(e)
            if isinstance(e, TrxNotFoundError):
                return Response(response=json.dumps({'message': e.message}), status=404, mimetype='application/json')
            raise e

    def register_routes(self):
        self.__routes = Blueprint('trx_controller', __name__)
        self.__routes.add_url_rule('/<trx_id>', 'get_trx_route', self.get_trx_route, methods=['GET'])

    def routes(self) -> Any:
        return self.__routes
