from flask import jsonify
from src.app import app
from src.models.database import db


@app.before_request()
def create_table():
    db.create_all()


@app.route("/api/auth/register", methods=['POST'])
def register_user():
    return jsonify("register")


@app.route("/api/auth/login", methods=['POST'])
def login_user():
    return jsonify("login")
