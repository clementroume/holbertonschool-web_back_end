#!/usr/bin/env python3
""" Session Authentication module
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session Authentication class.
    This class inherits from Auth and will be used for handling
    session-based authentication.
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session for a user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            str: The session ID, or None if user_id is None.
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
