import os

from dependency_injector import containers, providers

from src.application.use_cases.get_transaction.get_transaction import GetTransactionUseCase
from src.infrastructure.http.trx_controller import TrxController
from src.infrastructure.persistence.firestore.firestore_handler import FirestoreHandler
from src.infrastructure.config.config import app_config
from src.infrastructure.persistence.firestore.firestore_parser import FirestoreParser
from src.infrastructure.persistence.firestore.firestore_repository import FirestoreRepository


class Container(containers.DeclarativeContainer):
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

    trx_use_cases = providers.Singleton(
        GetTransactionUseCase,
        trx_repository
    )

    trx_controller = providers.Singleton(
        TrxController,
        trx_use_cases
    )