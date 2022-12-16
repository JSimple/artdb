from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app import db
from models.file import File

class Version(File):
    __tablename__= "versions"
    
    height = db.Column()
    width = db.Column()
    
    db.relationship(
        "Piece", backref="selected_version", lazy=True, primaryjoin="Piece.selected_version_id == Version.id", 
    )
    
class VersionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Version
        include_fk = True
        load_instance = True
        exclude = ("piece")