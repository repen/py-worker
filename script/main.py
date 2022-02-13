"""
Copyright 2022 Andrey Plugin (9keepa@gmail.com)
Licensed under the Apache License v2.0
http://www.apache.org/licenses/LICENSE-2.0
"""
import argparse, os


def script(name='default'):
    # ------ init var
    from config import config
    from database import AppDatabase
    conf = config[name]
    database = AppDatabase.init_database(conf)
    # ----------------
    from logic import Work
    from tool import log
    # log with file
    # logger = log("Main", os.path.join(conf.APP_DIR, "log/main.log"))
    logger = log("Main")
    logger.info(f"> Starting work the script with configuration [{name}]")
    work = Work(conf, database)
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
    script(args.config)
