from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    result = []
    for key in users.keys():
        result.append(key)
    return jsonify(result)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def user(username):
    user = users.get(username)
    if user is not None:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user",  methods=["POST"])
def add_user():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if username is None:
        return jsonify({"error": "Username is required"}), 400

    user = users.get(username)
    if user is not None:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = {}

    for key, value in data.items():
        users[username][key] = value

    return {
        "message": "User added",
        "user": data}


if __name__ == "__main__":
    app.run()
