from dependency_injector import containers, providers
from pymongo import MongoClient as MongoLibrary
from src.Services import MongoClient
from src.Repositories import MovieRepository

class IocContainer(containers.DeclarativeContainer):
    config = providers.Configuration('config')

    database_client = providers.Singleton(MongoLibrary, config.database.mongo_uri)

    db_mongo = providers.Factory(MongoClient.MongoClient, client=database_client, dbName='xuplau', collectionName='movies')

    main = providers.Callable(MovieRepository.MovieRepository, db_mongo=db_mongo)

