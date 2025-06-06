#!/usr/bin/env python3
"""Authentication module for API v1."""
from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication class for API v1."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if the path requires authentication."""
        return False

    def authorization_header(self, request=None) -> str:
        """Return the Authorization header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user from the request."""
        return None
