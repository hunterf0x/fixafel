"""IoC container module."""
import os

from dependency_injector import containers, providers

from src.application.use_cases.get_list_transactions.get_list_transactions import (
    GetListTransactionsUseCase)
from src.application.use_cases.get_transaction.get_transaction import GetTransactionUseCase
from src.infrastructure.config.config import app_config
from src.infrastructure.http.trx_controller import TrxController
from src.infrastructure.persistence.firestore.firestore_handler import FirestoreHandler
from src.infrastructure.persistence.firestore.firestore_parser import FirestoreParser
from src.infrastructure.persistence.firestore.firestore_repository import FirestoreRepository


class Container(containers.DeclarativeContainer):
    """IoC container for the application."""
    database_handler = providers.Singleton(
        FirestoreHandler,
        config=app_config[os.getenv('ENV')]
    )

    database_parser = providers.Singleton(
        FirestoreParser
    )

    trx_repository = providers.Singleton(
        FirestoreRepository,
        database_handler, database_parser
    )

    get_transaction_use_case = providers.Singleton(
        GetTransactionUseCase,
        trx_repository
    )

    get_list_transactions_use_case = providers.Singleton(
        GetListTransactionsUseCase,
        trx_repository
    )

    trx_controller = providers.Singleton(
        TrxController,
        get_transaction_use_case, get_list_transactions_use_case
    )
