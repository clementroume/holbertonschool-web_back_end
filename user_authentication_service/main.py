#!/usr/bin/env python3
"""
End-to-end integration test for the user authentication service.
"""
import requests

# The base URL for the running Flask application.
BASE_URL = "http://localhost:5050"


def register_user(email: str, password: str) -> None:
    """
    Tests the user registration endpoint.
    """
    payload = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/users", data=payload)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Tests logging in with an incorrect password.
    """
    payload = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/sessions", data=payload)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """
    Tests logging in with correct credentials and returns the session ID.
    """
    payload = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/sessions", data=payload)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "logged in"}
    session_id = response.cookies.get("session_id")
    assert session_id is not None
    return session_id


def profile_unlogged() -> None:
    """Tests that the profile endpoint is protected when not logged in."""
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    Tests that the profile endpoint is accessible with a valid session.
    """
    cookies = {"session_id": session_id}
    response = requests.get(f"{BASE_URL}/profile", cookies=cookies)
    assert response.status_code == 200
    assert response.json() == {"email": EMAIL}


def log_out(session_id: str) -> None:
    """
    Tests the logout functionality.
    """
    cookies = {"session_id": session_id}
    response = requests.delete(f"{BASE_URL}/sessions",
                               cookies=cookies,
                               allow_redirects=False)
    assert response.status_code == 302


def reset_password_token(email: str) -> str:
    """
    Tests the password reset token generation.
    """
    payload = {"email": email}
    response = requests.post(f"{BASE_URL}/reset_password", data=payload)
    assert response.status_code == 200
    reset_token = response.json().get("reset_token")
    assert reset_token is not None
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Tests updating the password with a valid reset token.
    """
    payload = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    }
    response = requests.put(f"{BASE_URL}/reset_password", data=payload)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
