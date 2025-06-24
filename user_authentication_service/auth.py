#!/usr/bin/env python3
"""Database module for user authentication service."""

from bcrypt import checkpw, hashpw, gensalt


def _hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return hashpw(password.encode('utf-8'), gensalt())
