#!/usr/bin/env python3
"""Database module for user authentication service."""

from bcrypt import hashpw, gensalt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> str:
        """Hash a password using bcrypt."""
        return hashpw(password.encode('utf-8'), gensalt())

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with email and password."""

        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exist")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            return self._db.add_user(email, hashed_password)
