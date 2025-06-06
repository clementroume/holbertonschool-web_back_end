#!/usr/bin/env python3
"""Authentication module for API v1."""
from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication class for API v1."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if the path requires authentication."""
        if path is None or not excluded_paths:
            return True

        # Normalize paths by ensuring they end with a slash
        if not path.endswith('/'):
            path += '/'

        # Normalize excluded paths by ensuring they end with a slash
        excluded_paths = [p if p.endswith('/') else
                          p + '/' for p in excluded_paths]

        return not any(path.startswith(excluded_path) for excluded_path
                       in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """Return the Authorization header from the request."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user from the request."""
        return None
