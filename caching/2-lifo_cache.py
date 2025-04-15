#!/usr/bin/python3
"""
LIFOCache module
"""
# Importing the BaseCaching class from base_caching module
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching
    """
    def __init__(self):
        """
        Initialize the LIFOCache instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using FIFO replacement policy
        """
        if key is None or item is None:
            return

        # If key already exists, just update it (FIFO order is not changed)
        if key in self.cache_data:
            del self.cache_data[key]
            self.cache_data[key] = item
            return

        # If we reached the cache limit, remove the first inserted item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            print("DISCARD: {}".format(last_key))
            del self.cache_data[last_key]

        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        return self.cache_data.get(key, None)
