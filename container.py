from pymongo import MongoClient as MongoLibrary
from dependency_injector import containers, providers
from src.Infrastructure import MongoClient
import InsertData

class IocContainer(containers.DeclarativeContainer):
    config = providers.Configuration('config')

    database_client = providers.Singleton(MongoLibrary, config.database.mongo_uri)

    db_mongo = providers.Factory(MongoClient.MongoClient, client=database_client)

    main = providers.Callable(InsertData.InsertData, db_mongo=db_mongo)

