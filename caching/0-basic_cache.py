#!/usr/bin/python3
"""
BasicCache module
"""
# Importing the BaseCaching class from base_caching module
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching
    """
    def __init__(self):
        """
        Initialize the BasicCache instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        if key:
            return self.cache_data.get(key)
        return None
