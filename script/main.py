"""
Copyright 2022 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""
import argparse


def script(config):
    from database import AppDatabase
    AppDatabase.init_database(config)
    from logic import Work
    from tool import log
    logger = log(__name__)
    logger.info(f"> Starting work the script with configuration [{config.ENV}]")
    work = Work(config, AppDatabase())
    work.run()
    logger.info(f"< End worked the script")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Running the application.'
    )

    parser.add_argument('-c', '--config', dest='config', type=str, default="default",
                        help='An example:\npython main.py --config production|development|testing|default')

    args = parser.parse_args()

    from config import config

    conf = config[args.config]

    args_dict = {k.upper():v for k,v in vars(args).items()}
    for k, v in args_dict.items():
        setattr(conf, k, v)

    script(conf)
