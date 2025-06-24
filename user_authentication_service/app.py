#!/usr/bin/env python3
"""Database module for user authentication service."""

from flask import Flask, Response, jsonify, request, abort, redirect
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

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id: str = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout() -> Response:
    """Logout a user by clearing their session."""
    session_id: str = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect("/")


@app.route('/profile', methods=['GET'])
def profile() -> Response:
    """Get the profile of the logged-in user."""
    session_id: str = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    return jsonify({"email": user.email})


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token() -> Response:
    """Generate a reset password token for a user."""
    email: str = request.form.get('email')

    try:
        reset_token: str = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token})
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password() -> Response:
    """Update a user's password using a reset token."""
    email: str = request.form.get('email')
    reset_token: str = request.form.get('reset_token')
    password: str = request.form.get('new_password')

    try:
        AUTH.update_password(reset_token, password)
    except ValueError:
        abort(403)

    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5050")
