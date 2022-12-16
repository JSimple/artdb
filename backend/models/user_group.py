from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app import db
from models.base import Base, create_association_table


pieces_user_groups = create_association_table(
    "pieces_user_groups",
    "user_groups",
    "pieces",
    "user_group_id",
    "piece_id",
)

class UserGroup(Base):
    __tablename__ = "user_groups"

    name = db.Column(db.String(225), nullable=False, unique=True)

    pieces = db.relationship(secondary=pieces_user_groups)

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserGroup
        include_relationships = True
        load_instance = True
