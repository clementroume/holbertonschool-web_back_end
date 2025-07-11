#!/usr/bin/env python3
"""Exercise Module"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Cache class to handle Redis operations."""

    def __init__(self):
        """Initialize the Cache with a Redis connection."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[
                str, bytes, int, float, None
    ]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key: The string key for the data.
            fn: An optional callable to convert the data
                back to the desired format.

        Returns:
            The data stored in Redis, converted if a function is provided,
            or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string value from Redis.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer value from Redis.
        """
        return self.get(key, fn=int)
