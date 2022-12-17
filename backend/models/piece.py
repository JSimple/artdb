from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from config import db
from models.base import Base


class Piece(Base):
    __tablename__ = "pieces"

    title = db.Column(db.String(500), nullable=False)
    info = db.Column(db.Text, default="", nullable=False)
    info_updated = db.Column(db.DateTime, default=db.func.current_timestamp())

    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    selected_title_id = db.Column(db.Integer, db.ForeignKey("titles.id"), nullable=True)
    selected_version_id = db.Column(
        db.Integer, db.ForeignKey("versions.id"), nullable=True
    )

    selected_version = db.relationship(
        "Version",
        foreign_keys=selected_version_id,
        lazy=True,
    )

    versions = db.relationship(
        "Version",
        foreign_keys="Version.piece_id",
        backref="piece",
        lazy=True,
        cascade="all, delete-orphan",
    )

    suggested_titles = db.relationship(
        "Title", backref="piece", lazy=True, cascade="all, delete-orphan"
    )


# class PieceSchema(SQLAlchemyAutoSchema):
#     class Meta:
#         model = Piece
#         include_relationships = True
#         load_instance = True
