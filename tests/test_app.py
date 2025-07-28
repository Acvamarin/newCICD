from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

# Определите маршруты для добавления и получения пользователей
@app.route('/users', methods=['POST'])
def add_user():
    # Ваш код для добавления пользователя

@app.route('/users', methods=['GET'])
def get_users():
    # Ваш код для получения пользователей
