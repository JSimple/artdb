from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app import db
from models.base import Base


class User(Base):
    __tablename__= "users"
    
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    
    pieces = db.relationship(
    "Piece", backref="author", lazy=True, cascade="all, delete-orphan"
    )

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ("pieces")
        load_instance = True