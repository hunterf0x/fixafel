"""This module defines the IoC container for the application.

It uses the `dependency_injector` library to manage the dependencies and
provide singleton instances of various components such as handlers, parsers,
repositories, use cases, and controllers.
"""

import os
from dependency_injector import containers, providers
from application.use_cases.get_list_transactions.get_list_transactions import GetListTransactionsUseCase
from application.use_cases.get_transaction.get_transaction import GetTransactionUseCase
from application.use_cases.reinject_transactions.reinject_transactions import ReinjectTransactionsUseCase
from infrastructure.config.config import app_config
from infrastructure.http.trx_controller import TrxController
from infrastructure.logger.logger_config import get_logger
from infrastructure.persistence.firestore.firestore_handler import FirestoreHandler
from infrastructure.persistence.firestore.firestore_parser import FirestoreParser
from infrastructure.persistence.firestore.firestore_repository import FirestoreRepository


class Container(containers.DeclarativeContainer):
    """IoC container for managing application dependencies.

    This container provides singleton instances of the following components:
    - FirestoreHandler: Handles database operations.
    - FirestoreParser: Parses Firestore data.
    - FirestoreRepository: Repository for Firestore operations.
    - GetTransactionUseCase: Use case for getting a single transaction.
    - GetListTransactionsUseCase: Use case for getting a list of transactions.
    - TrxController: Controller for transaction-related HTTP endpoints.
    """

    logger = providers.Singleton(
        get_logger,
        name=__name__
    )

    database_handler = providers.Singleton(
        FirestoreHandler,
        config=app_config[os.getenv('ENV')]
    )

    database_parser = providers.Singleton(
        FirestoreParser
    )

    trx_repository = providers.Singleton(
        FirestoreRepository,
        database_handler, database_parser,
        logger=logger
    )

    get_transaction_use_case = providers.Singleton(
        GetTransactionUseCase,
        trx_repository,
        logger=logger
    )

    get_list_transactions_use_case = providers.Singleton(
        GetListTransactionsUseCase,
        trx_repository,
        logger=logger
    )

    reinject_transactions_use_case = providers.Singleton(
        ReinjectTransactionsUseCase,
        trx_repository,
        logger=logger
    )

    trx_controller = providers.Singleton(
        TrxController,
        get_transaction_use_case, get_list_transactions_use_case, reinject_transactions_use_case,
        logger=logger
    )
