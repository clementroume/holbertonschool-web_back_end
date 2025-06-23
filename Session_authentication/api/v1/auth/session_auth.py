#!/usr/bin/env python3
""" Session Authentication module
"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session Authentication class.
    This class inherits from Auth and will be used for handling
    session-based authentication.
    """
