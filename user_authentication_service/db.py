#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database
        """
        new_user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(new_user)
        session.commit()
        session.refresh(new_user)

        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by given attributes
        """
        session = self._session
        user = session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound("No user found with the given attributes")
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user by user_id with given attributes
        """
        session = self._session

        user = self.find_user_by(id=user_id)

        if not user:
            raise NoResultFound("No user found with the given user_id")

        for key, value in kwargs.items():
            if key not in User.__table__.columns.keys():
                raise ValueError(f"Invalid attribute: {key}")
            setattr(user, key, value)

        session.commit()
