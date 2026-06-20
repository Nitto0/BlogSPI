from flask import jsonify
from src.app import app
from src.models.database import db
from src.models.post import Post


@app.route("/api/posts", methods=['GET'])
def get_posts():
    return jsonify("get posts")
