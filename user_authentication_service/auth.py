#!/usr/bin/env python3
"""Database module for user authentication service."""


def _hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    import bcrypt

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')
