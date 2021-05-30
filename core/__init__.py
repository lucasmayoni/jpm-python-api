from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:secret@172.21.0.200:3306/juguetes'
db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()


from api import items, categories