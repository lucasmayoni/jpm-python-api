from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from core import app, db


class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20))
    description = db.Column(db.String(100))
    provider_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer)
    price = db.Column(db.Float)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, code, description, provider_id, category_id, price):
        self.code = code
        self.description = description,
        self.provider_id = provider_id
        self.category_id = category_id
        self.price = price

    def __repr__(self):
        return f"{self.id, self.description}"


class ItemSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Item
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    code = fields.String(required=True)
    description = fields.String(required=True)
    provider_id = fields.Integer(required=True)
    category_id = fields.Integer(required=True)
    price = fields.Float(required=True)

