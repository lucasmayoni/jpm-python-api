from core import app, db


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=3000, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
