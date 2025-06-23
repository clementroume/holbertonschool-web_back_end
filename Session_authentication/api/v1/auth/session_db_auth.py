#!/usr/bin/env python3
""" Session Authentication DB module"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """Session DB Authentication class.
    This class extends SessionExpAuth to handle session storage in a database.
    """

    def __init__(self):
        """Initialize the SessionDBAuth instance."""
        super().__init__()

    def create_session(self, user_id=None):
        """Create a session and store it in the database."""
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        user_session = UserSession(user_id=user_id, session_id=session_id)

        if user_session is None:
            return None

        user_session.save()
        UserSession.save_to_file()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Retrieve the user ID for a session ID from the database."""
        if session_id is None:
            return None

        UserSession.load_from_file()
        user_session = UserSession.search({'session_id': session_id})

        if not user_session:
            return None

        user_session = user_session[0]

        if self.session_duration <= 0 or user_session.created_at is None:
            return user_session.user_id

        expired_at = user_session.created_at + \
            timedelta(seconds=self.session_duration)

        if datetime.now() > expired_at:
            return None

        return user_session.user_id

    def destroy_session(self, request=None):
        """Destroy a session and remove it from the database."""
        if request is None:
            return False

        session_id = self.session_cookie(request)

        if session_id is None:
            return False

        user_session = UserSession.search({'session_id': session_id})

        if not user_session:
            return False

        user_session = user_session[0]
        user_session.remove()
        UserSession.save_to_file()

        return True
