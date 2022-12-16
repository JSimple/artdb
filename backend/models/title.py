from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app import db
from models.base import Base

class Title(Base):
    __tablename__= "versions"
    
    text = db.Column(db.String(500), nullable=False)
    
    db.relationship(
        "Piece", backref="selected_title", lazy=True, primaryjoin="Piece.selected_title_id == Title.id", 
    )
    
class VersionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Title
        include_fk = True
        load_instance = True
        exclude = ("piece")