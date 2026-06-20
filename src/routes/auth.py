from flask import jsonify, request, abort
from src.app import app
from src.models.user import User
from src.models.database import db
from pydantic import ValidationError
from src.schemas.UserSchema import UserSchema


@app.route("/api/users", methods=['GET'])
def get_users():
    users_list = []
    for user in User.query.all():
        users_list.append({'id': user.id, 'username': user.username, 'email': user.email,
                           'password': user.password_hash, 'created_at': user.created_at})

    return jsonify({
        "users": users_list
    }), 200


@app.route("/api/auth/register", methods=['POST'])
def register_user():
    new_user = request.json
    if 'username' not in new_user or 'email' not in new_user or 'password' not in new_user:
        abort(400, description="You should write username, email and password!")

    try:
        validate_user = UserSchema(username=new_user['username'], email=new_user['email'],
                                   password=new_user['password'])
        print(f'''Success validation! 
                        Name: {validate_user.username}, 
                        email: {validate_user.email}
                        password: {validate_user.password}''')
    except ValidationError:
        abort(400, description="Validation error!")

    user = User(username=new_user['username'], email=new_user['email'],
                password_hash=new_user['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "created_at": user.created_at
    }), 201


@app.route("/api/auth/login", methods=['POST'])
def login_user():
    auth_user = request.json
    if 'username' not in auth_user or 'email' not in auth_user or 'password' not in auth_user:
        abort(400, description="You should write username, email and password!")

    return jsonify("login")
