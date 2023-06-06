# models.py

from datetime import datetime
# imports db, an instance of SQLAlchemy that's defined in config.py
from config import db, ma


# inheriting the db.Model gives Person the SQLAlchemy features to connect to the db and access its tables
class Person(db.Model):
    # connects the class definition to the person database table
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key = True)
    lname = db.Column(db.String(32), unique = True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class PersonSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Person
        # ability to deserialize JSON data and load Person model instances from it
        load_instance = True
        sqla_session = db.session


person_schema = PersonSchema()
people_schema = PersonSchema(many=True)