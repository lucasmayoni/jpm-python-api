from core import app
from models.item import db, Item, ItemSchema
from flask import jsonify, make_response, request


@app.route('/items', methods=['GET'])
def index():
    get_items = Item.query.all()
    item_schema = ItemSchema(many=True)
    items = item_schema.dump(get_items)
    return make_response(jsonify({"items": items}), 200)


@app.route('/items/<id>', methods=['GET'])
def get_by_id(id):
    get_item = Item.query.get(id)
    item_schema = ItemSchema()
    item = item_schema.dump(get_item)
    return make_response(jsonify(item), 200)


@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    item_schema = ItemSchema()
    item = item_schema.load(data)
    result = item_schema.dump(item.create())
    return make_response(jsonify({'item': result}), 200)
