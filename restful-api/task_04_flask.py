#!/usr/bin/env python3
"""
This module implements a simple Flask API that manages users and
provides basic endpoints for data retrieval and status checks.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """
    Returns a welcome message for the API.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """
    Returns a list of all registered usernames.
    """
    result = []
    for key in users.keys():
        result.append(key)
    return jsonify(result)


@app.route("/status")
def status():
    """
    Returns the status of the API.
    """
    return "OK"


@app.route("/users/<username>")
def user(username):
    """
    Returns user information for a given username.
    """
    user = users.get(username)
    if user is not None:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user to the API using JSON data from the request body.
    """
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

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
