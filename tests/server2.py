from flask import Flask, jsonify
import random
import uuid
from datetime import datetime

app = Flask(__name__)

@app.route('/api/types', methods=['GET'])
def get_various_types():
    """Return a response with various data types"""
    return jsonify({
        "integer_value": random.randint(1, 100),
        "string_value": f"Random string {random.randint(1000, 9999)}",
        "boolean_value": random.choice([True, False]),
        "float_value": random.uniform(1.0, 100.0),
        "array_value": [random.randint(1, 10) for _ in range(3)],
        "object_value": {
            "nested_key": "nested value",
            "timestamp": datetime.now().isoformat()
        },
        "null_value": None
    })


@app.route('/api/user/<username>', methods=['GET'])
def get_user(username):
    """Return user information with various formatted fields"""
    user_id = str(uuid.uuid4())
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return jsonify({
        "id": user_id,
        "username": username,
        "email": f"{username}@example.com",
        "phone": "555-123-4567",
        "created_at": current_time,
        "profile_url": f"https://example.com/users/{username}",
        "status": "Active",
        "account_number": "ACC-" + "".join([str(i) for i in range(10)]),
        "comments": [
            "First comment by user",
            "Another comment with some numbers 123",
            "Comment with special chars: $#@!"
        ]
    })

@app.route('/api/users', methods=['GET'])
def get_users():
    # Return a sample list of users
    users = [
        {
            "id": 1,
            "name": "Alice",
            "email": "alice@example.com",
            "roles": ["admin", "user"]
        },
        {
            "id": 2,
            "name": "Bob",
            "email": "bob@example.com",
            "roles": ["user"]
        }
    ]
    return jsonify({"users": users})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)