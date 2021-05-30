from core import app
from models.category import db, Category, CategorySchema
from flask import jsonify, make_response, request


@app.route('/categories', methods=['GET'])
def list_categories():
    get_categories = Category.query.all()
    category_schema = CategorySchema(many=True)
    categories = category_schema.dump(get_categories)
    return make_response(jsonify({"categories": categories}), 200)