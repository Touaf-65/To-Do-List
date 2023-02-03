from flask import Flask
from views import index, delete, update, about
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db.init_app(app)

app.add_url_rule("/", "index", index)
app.add_url_rule("/delete/<int:id>/", "delete", delete)
app.add_url_rule("/update/<int:id>/", "update", update, methods=["GET", "POST"])
app.add_url_rule("/about/", "about", about)
