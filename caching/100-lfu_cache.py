#!/usr/bin/python3
"""
LFUCache module
"""
from collections import defaultdict, OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching
    and uses Least Frequently Used (LFU) caching strategy
    """
    def __init__(self):
        """
        Initialize the LFUCache instance
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.freq_counter = defaultdict(int)  # key: frequency

    def put(self, key, item):
        """
        Add an item to the cache using LFU replacement policy
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update existing key
            self.cache_data[key] = item
            self.freq_counter[key] += 1

        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the key(s) with the lowest frequency
                min_freq = min(self.freq_counter.values())
                candidates = [k for k in self.cache_data
                              if self.freq_counter[k] == min_freq]

                # Among candidates, discard the one inserted first
                discard_key = candidates[0]
                print("DISCARD: {}".format(discard_key))
                del self.cache_data[discard_key]
                del self.freq_counter[discard_key]

            # Insert new key
            self.cache_data[key] = item
            self.freq_counter[key] = 1

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.freq_counter[key] += 1
        return self.cache_data[key]
