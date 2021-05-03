from core import app
from models.item import db, Item, ItemSchema
from flask import jsonify, make_response


@app.route('/items', methods=['GET'])
def index():
    get_items = Item.query.all()
    item_schema = ItemSchema(many=True)
    items = item_schema.dump(get_items)
    return make_response(jsonify({"items": items}), 200)
