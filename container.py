from pymongo import MongoClient
from dependency_injector import containers, providers
from src.Infrastructure import MongoConnection
import InsertData

class IocContainer(containers.DeclarativeContainer):
    config = providers.Configuration('config')

    database_client = providers.Singleton(MongoClient, config.database.mongo_uri)

    db_mongo = providers.Factory(MongoConnection.MongoConnection, client=database_client)

    main = providers.Callable(InsertData.InsertData, db_mongo=db_mongo)

