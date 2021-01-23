# Imports
import os
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv(find_dotenv())


"""
SETUP ACCESS TO MYSQL DB ON DREAMHOST"""
hostname = os.getenv("hostname")
username = os.getenv("username")
password = os.getenv("password")
database = os.getenv("database")


# Create connection string for MySQL db on Dreamhost
creds = ("mysql://", username, ":", "password", "@", hostname, "/", database)
url = "".join(creds)


engine = create_engine(url, encoding='latin1', echo=True)


Session = sessionmaker()
sess = Session(bind=engine)
Base = declarative_base()
