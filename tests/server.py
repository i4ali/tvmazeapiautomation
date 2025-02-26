# app.py
from flask import Flask, jsonify, request, make_response
from functools import wraps
import uuid

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "Flask server is running!", 200


@app.route('/square', methods=['POST'])
def square_endpoint():
    data = request.get_json()
    a = data.get('a')
    try:
        a = float(a)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid numbers provided"}), 400
    result = a ** 2
    return jsonify({"result": result}), 200


@app.route('/reverse', methods=['POST'])
def reverse_endpoint():
    data = request.get_json()
    s = data.get('s')
    if not isinstance(s, str):
        return jsonify({"error": "Invalid string provided"}), 400
    reversed_string = s[::-1]  # Reverse the string using slicing
    return jsonify({"result": reversed_string}), 200


@app.route('/user', methods=['GET'])
def get_user():
    """Endpoint that returns different responses based on query params"""
    minimal = request.args.get('minimal', 'false').lower() == 'true'

    base_response = {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com"
    }

    if minimal:
        return jsonify({k: base_response[k] for k in ['id', 'name']})

    return jsonify(base_response)


# In-memory storage for demonstration
valid_tokens = set()
users = {
    "test_user": {
        "password": "secure_password",
        "email": "test@example.com"
    }
}


# Authentication decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split("Bearer ")[-1]

        if not token or token not in valid_tokens:
            return jsonify({"message": "Invalid token"}), 401

        return f(*args, **kwargs)

    return decorated


@app.route('/auth', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)
    if not user or user['password'] != password:
        return jsonify({"message": "Invalid credentials"}), 401

    # Generate token
    token = str(uuid.uuid4())
    valid_tokens.add(token)

    return jsonify({"access_token": token})


@app.route('/auth/logout', methods=['POST'])
@token_required
def logout():
    token = request.headers['Authorization'].split("Bearer ")[-1]
    valid_tokens.discard(token)
    return '', 204


@app.route('/profile', methods=['GET'])
@token_required
def get_profile():
    token = request.headers['Authorization'].split("Bearer ")[-1]
    # In real app, get user from token
    return jsonify({
        "username": "test_user",
        "email": "test@example.com"
    })


if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
