#!/usr/bin/env python3
""" Basic Authentication module
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Authentication class.

    This class inherits from Auth and will be used for handling
    HTTP Basic Authentication.
    """
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """Extracts the Base64 part of the Authorization header.

        Args:
            authorization_header (str): The Authorization header.

        Returns:
            str: The Base64 part of the header, or None if not valid.
        """
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        if " " in authorization_header:
            return authorization_header.split(" ", 1)[1]
        return None
