from config import db
import sqlalchemy


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )


def create_association_table(
    table_name: str,
    left_table: str,
    right_table: str,
    left_id: str,
    right_id: str,
) -> sqlalchemy.schema.Table:
    return db.Table(
        table_name,
        Base.metadata,
        db.Column(left_id, db.ForeignKey(f'{left_table}.id')),
        db.Column(right_id, db.ForeignKey(f'{right_table}.id')),
    )
