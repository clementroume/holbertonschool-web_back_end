#!/usr/bin/env python3
"""Database module for user authentication service."""

from flask import Flask, Response, jsonify, request, make_response, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def index() -> Response:
    """Index route for the API."""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def user() -> Response:
    """Register a new user."""
    email: str = request.form.get('email')
    password: str = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login() -> Response:
    """Create a session for a user."""
    email: str = request.form.get('email')
    password: str = request.form.get('password')

    if not email or not password:
        abort(400)

    if AUTH.valid_login(email, password):
        session_id: str = AUTH.create_session(email)
        if not session_id:
            abort(401)
        response = make_response(
            jsonify({"email": email, "message": "logged in"}))
        response.set_cookie("session_id", session_id, path="/")
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5050")
