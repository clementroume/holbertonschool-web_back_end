#!/usr/bin/env python3
""" Session Authentication Expiration module"""

from api.v1.auth.session_auth import SessionAuth
import os
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """Session Expiration Authentication class.
    This class extends SessionAuth to handle session expiration.
    """

    def __init__(self):
        """Initialize the SessionExpAuth instance."""
        super().__init__()
        SESSION_DURATION = os.getenv('SESSION_DURATION')
        if SESSION_DURATION is None:
            self.session_duration = 0
        else:
            self.session_duration = int(SESSION_DURATION)

    def create_session(self, user_id=None):
        """Create a session with an expiration time."""
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        self.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()}

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Retrieve the user ID for a session ID, considering expiration."""

        if not session_id or session_id not in self.user_id_by_session_id:
            return None

        session_data = self.user_id_by_session_id.get(session_id)

        if self.session_duration <= 0 or session_data is None:
            return None

        created_at = session_data.get('created_at')
        if created_at is None:
            return None

        expired_At = created_at + \
            timedelta(seconds=self.session_duration)

        if datetime.now() > expired_At:
            return None

        return session_data.get('user_id')
