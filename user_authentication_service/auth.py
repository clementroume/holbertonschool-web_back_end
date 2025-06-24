#!/usr/bin/env python3
"""Database module for user authentication service."""

import uuid

from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
    """Generate a unique identifier (UUID) for session or reset token."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with email and password."""

        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exist")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate a user's login credentials."""
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a session for a user."""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Get a user by their session ID."""
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy a user's session by user ID."""
        self._db.update_user(user_id, session_id=None)
