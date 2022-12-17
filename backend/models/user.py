from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from config import db
from models.base import create_association_table
from models.base import Base

users_groups = create_association_table(
    "users_groups",
    "users",
    "groups",
    "user_id",
    "group_id",
)

class User(Base):
    __tablename__= "users"
    
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    
    pieces = db.relationship(
    "Piece", backref="author", lazy=True, cascade="all, delete-orphan"
    )
    
    groups = db.relationship("Group",secondary=users_groups)


    
# class UserSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = User
#         exclude = ("pieces",)
#         load_instance = True