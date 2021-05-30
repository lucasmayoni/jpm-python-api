from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from core import app, db


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100))
    color = db.Column(db.String(50))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return

    def __init__(self, code, description, color):
        self.code = code
        self.description = description,
        self.color = color

    def __repr__(self):
        return f"{self.id, self.description}"


class CategorySchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Category
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    code = fields.String(required=True)
    color = fields.String(required=True)
