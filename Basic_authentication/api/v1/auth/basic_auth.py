#!/usr/bin/env python3
""" Basic Authentication module
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
import base64
from models.user import User


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

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Decodes the Base64 part of the Authorization header.

        Args:
            base64_authorization_header (str): The Base64 Authorization header.

        Returns:
            str: The decoded string, or None if not valid.
        """
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return (
                base64.b64decode(base64_authorization_header).decode("utf-8")
            )
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
            ) -> (str, str):
        """Extracts user credentials from the decoded
        Base64 Authorization header.

        Args:
            decoded_base64_authorization_header (str):
            The decoded Base64 header.

        Returns:
            tuple: A tuple containing the username and
            password, or (None, None) if not valid.
        """
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """Returns the User instance based on email and password.

        Args:
            user_email (str): The user's email.
            user_pwd (str): The user's password.

        Returns:
            User: The User object, or None if invalid.
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if not users:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None
