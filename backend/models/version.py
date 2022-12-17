from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from config import db
from models.file import File


class Version(File):
    __tablename__ = "versions"

    height = db.Column(db.Integer)
    width = db.Column(db.Integer)




# class VersionSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = Version
#         include_fk = True
#         load_instance = True
#         exclude = ("piece",)
