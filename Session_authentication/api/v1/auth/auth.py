#!/usr/bin/env python3
"""Authentication module for API v1."""
from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication class for API v1."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if the path requires authentication.

        This method now supports wildcards (*) at the end of excluded paths.
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True

        # Ensure path has a trailing slash for consistent matching
        normalized_path = path if path.endswith('/') else path + '/'

        for excluded_path in excluded_paths:
            # If the excluded path ends with a wildcard
            if excluded_path.endswith('*'):
                # Get the prefix by removing the wildcard
                prefix = excluded_path[:-1]
                # Check if the request path starts with this prefix
                if path.startswith(prefix):
                    return False  # Authentication not required
            # Otherwise, use exact matching with normalized paths
            elif normalized_path == excluded_path:
                return False  # Authentication not required

        # If no match was found in the loop, authentication is required
        return True

    def authorization_header(self, request=None) -> str:
        """Return the Authorization header from the request."""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the current user from the request."""
        return None
