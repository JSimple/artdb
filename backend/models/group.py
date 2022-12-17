from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from config import db
from models.base import Base, create_association_table


pieces_groups = create_association_table(
    "pieces_groups",
    "groups",
    "pieces",
    "group_id",
    "piece_id",
)

class Group(Base):
    __tablename__ = "groups"

    name = db.Column(db.String(225), nullable=False, unique=True)

    pieces = db.relationship("Piece", secondary=pieces_groups)

# class UserSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = Group
#         include_relationships = True
#         load_instance = True
#         exclude = ("pieces","users")
