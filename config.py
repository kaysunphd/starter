import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'connect-to-storage-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'connect-to-storage-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'udacitycloudadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'qwerty314!'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'connecttostorageblob'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'O2GEf9h3j44yGR8Lum4J5jwZ3OjamnR6h+KIMU4K90zIpQkNvpqJArfA5T/5RU1nbRc7uMXlsbBxtEz2ZD3Lqw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
