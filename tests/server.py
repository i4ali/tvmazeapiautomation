from flask import Flask, request, jsonify

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


if __name__ == '__main__':
    app.run(debug=True)
