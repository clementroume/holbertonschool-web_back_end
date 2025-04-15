#!/usr/bin/python3
"""
MRUCache module
"""
from collections import OrderedDict
# Importing the BaseCaching class from base_caching module
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching
    and uses Most Recently Used (MRU) caching strategy
    """
    def __init__(self):
        """
        Initialize the MRUCache instance
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache using MRU replacement policy
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Remove the existing key to update order later
            del self.cache_data[key]

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the most recently used item (last one)
            most_recent = next(reversed(self.cache_data))
            print("DISCARD: {}".format(most_recent))
            del self.cache_data[most_recent]

        # Insert as the most recently used
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the end to mark it as most recently used
        value = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = value
        return value
