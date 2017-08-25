import ConfigParser
import os

CONFIG_PARSER = ConfigParser.ConfigParser()
PROJECT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir, os.pardir)


class Config:
    def __init__(self):
        config_file = os.path.join(PROJECT_ROOT, 'testconfig', 'local', 'project.ini')
        CONFIG_PARSER.read(config_file)

    def mysql_config(self):
        return {
            "database_name": CONFIG_PARSER.get("database", "PROJECT_DB_NAME"),
            "database_user": CONFIG_PARSER.get("database", "PROJECT_DB_ADMIN"),
            "database_user_password": CONFIG_PARSER.get("database", "PROJECT_DB_PASS")
        }
