"""
Copyright 2021 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""

import os
from config import BaseEnvironment, ProductionEnvironment, \
    DevelopmentEnvironment, TestingEnvironment
from typing import Union

class Database:
    def __init__(self, config: Union[BaseEnvironment, ProductionEnvironment,
                             DevelopmentEnvironment, TestingEnvironment]):
        self._db = None

    def get_db(self):
        return self._db



class AppDatabase:

    _db = None

    @staticmethod
    def init_database(config):
        return AppDatabase.get_db(config)

    @staticmethod
    def get_db(config: Union[BaseEnvironment, ProductionEnvironment,
                             DevelopmentEnvironment, TestingEnvironment]):
        if AppDatabase._db is None:
            AppDatabase._db = Database(config).get_db()
        return AppDatabase._db
