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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieves the user ID associated with a session ID.

        Args:
            session_id (str): The session ID.

        Returns:
            str: The user ID, or None if session_id is None or not found.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
