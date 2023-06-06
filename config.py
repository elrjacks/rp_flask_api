# config.py

import pathlib

import connexion
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
# point to the directory that the program in running in
basedir = pathlib.Path(__file__).parent.resolve()
# create the Connexion app instance and give it the path to the directory that contains the specification file
connex_app = connexion.App(__name__, specification_dir=basedir)

# flask instance initialized by connexion
app = connex_app.app
# tells SQLAlchemy to use sql lite as the db and a file name people.db in the current directory as the db file
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'people.db'}"
# turns the SQLAlchemy system off
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initializes SQLAlchemy by passing the app config info to SQLAlchemy and assigning the result to the db variable
db = SQLAlchemy(app)
# initializes Marshmallow and allows it to work with the SQLAlchemy components attached to the app
ma = Marshmallow(app)