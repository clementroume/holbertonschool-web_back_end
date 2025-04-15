#!/usr/bin/python3
"""
LRUCache module
"""
from collections import OrderedDict
# Importing the BaseCaching class from base_caching module
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching
    """
    def __init__(self):
        """
        Initialize the LRUCache instance
        """
        super().__init__()
        # We use an OrderedDict to maintain the order of insertion and access
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache using LRU replacement policy
        """
        if key is None or item is None:
            return

        # If key already exists, update it and move it to the end
        # (most recently used)
        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        # If we reached the cache limit, remove the least recently used item
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Pop the first item (least recently used)
            discarded_key, discarded_item = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(discarded_key))

        # Add the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed item to the end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
