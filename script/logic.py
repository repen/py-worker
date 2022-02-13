"""
Copyright 2022 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""
from config import DevelopmentEnvironment, ProductionEnvironment, TestingEnvironment
from typing import Union, Any
from tool import log


logger = log(__name__)


class Work:
    def __init__(self,
                 config: Union[DevelopmentEnvironment, ProductionEnvironment,
                     TestingEnvironment],
                 database: Any = None
                 ):
        self.config = config
        self.database = database

    def run(self) -> Any:
        """Entry point for your payloads
        """
        logger.debug(f"2 + 2 = {2+2}")
        a = 2 + 2
        return a

