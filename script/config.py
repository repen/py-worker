"""
Copyright 2021 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""
import os


class BaseEnvironment:
    ENV = "base"
    APP_DIR = os.getenv("APP_DIR", os.getcwd())
    PRODUCTION = False

    @staticmethod
    def init_env(env_dict: dict):
        for key, val in env_dict.items():
            os.environ[key] = str(val)


    @staticmethod
    def set_config_name(name):
        _config = {}
        cls = config[name]
        for key in dir(config[name]):
            if key.isupper():
                _config[key] = getattr(cls, key)
        BaseEnvironment.init_env(_config)


class ProductionEnvironment(BaseEnvironment):
    ENV = "production"
    PRODUCTION = True


class DevelopmentEnvironment(BaseEnvironment):
    ENV = "development"


class TestingEnvironment(BaseEnvironment):
    ENV = "testing"


config = {
    "development" : DevelopmentEnvironment,
    "testing" : TestingEnvironment,
    "production": ProductionEnvironment,
    "default" : DevelopmentEnvironment
}
