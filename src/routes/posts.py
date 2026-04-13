from flask import jsonify
from src.app import app


@app.route("/api/posts", methods=['GET'])
def get_posts():
    return jsonify("get posts")
