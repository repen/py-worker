from config import BaseEnvironment, ProductionEnvironment, \
    DevelopmentEnvironment, TestingEnvironment
from typing import Union
# from playhouse.pool import PooledMySQLDatabase

class Database:
    def __init__(self,
                 database_name="",
                 database_user="",
                 database_password="",
                 database_port="3600",
                 database_host="localhost"
                 ):

        # self.db = PooledMySQLDatabase(
        #     database_name,
        #     user=database_user,
        #     password=database_password,
        #     port=int(database_port),
        #     host=database_host,
        #     stale_timeout = None,
        #     max_connections=2,
        # )
        self.db = None

    def get(self):
        return self.db



class AppDatabase:

    _db = None

    @staticmethod
    def init_database(config: Union[TestingEnvironment, 
                                    DevelopmentEnvironment, ProductionEnvironment]):
        AppDatabase._init_database(config)

    @staticmethod
    def get_database():
        return AppDatabase._db

    @staticmethod
    def _init_database(config: Union[TestingEnvironment, 
                                     DevelopmentEnvironment, ProductionEnvironment]):

        AppDatabase._db = Database().get()
