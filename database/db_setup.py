from os import environ

from sqlalchemy import create_engine

DATABASE_HOST = environ['DATABASE_HOST']
DATABASE_USERNAME = environ['DATABASE_USERNAME']
DATABASE_PASSWORD = environ['DATABASE_PASSWORD']
DATABASE_NAME = environ['DATABASE_NAME']

CONNECTION_STRING = f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}?charset=utf8mb4"

engine = create_engine(CONNECTION_STRING,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})
