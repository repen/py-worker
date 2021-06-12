"""
Copyright 2021 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""
import argparse, os


def script(name='default'):
    from config import config
    from database import AppDatabase
    conf = config[name]
    database = AppDatabase.init_database(conf)

    from tool import log
    # logger = log("Main", os.path.join(conf.APP_DIR, "log/main.log"))
    logger = log("Main")
    logger.info(f"Start script with config {name}")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Running the application.'
    )

    parser.add_argument('-c', '--config', dest='config', type=str, required=True,
                        help='An example:\npython main.py --config development|testing|default')

    args = parser.parse_args()
    script(args.config)
