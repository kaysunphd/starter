import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="migrate-db-server.postgres.database.azure.com"
    POSTGRES_USER="migrateudacityadmin@migrate-db-server"
    POSTGRES_PW="qwerty314!"
    POSTGRES_DB="techconfdb"
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'  # not used
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://migrate.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=w0BuWEwMHJLutGco9/OJe7lSBIAse0jJgZN1b7/lzpA=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False