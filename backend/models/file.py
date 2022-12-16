
from app import db
from models.base import Base
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class File(Base):
    __abstract__= True
    
    storage_id = db.Column(db.String, default=generate_uuid)
    name = db.Column(db.String(225), nullable=False)
    upload_name = db.Column(db.String(225), nullable=False)
    mimetype = db.Column(db.String(225), nullable=False)
    size = db.Column(db.Float, nullable=False)
    
    piece_id = db.Column(db.Integer, db.ForeignKey("pieces.id"), nullable=False)