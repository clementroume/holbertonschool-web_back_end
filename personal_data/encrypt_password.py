#!/usr/bin/env python3
"""
This module provides functionality for securely hashing passwords using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt and a randomly generated salt.

    Args:
        password (str): the password to hash.

    Returns:
        bytes: the hashed password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
