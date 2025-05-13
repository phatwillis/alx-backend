#!/usr/bin/env python3
"""implementin basic caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Cache class"""

    def __init__(self):
        """initialiser"""
        super().__init__()

    def put(self, key, item):
        """sets keys to item
        and saves to cache data"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item
        # if cache data has more than max items,
        # implement first in first out
        if len(self.cache_data) > self.MAX_ITEMS:
            # return a list representation of the keys in cache_data
            list_of_keys = list(self.cache_data)
            first_key = list_of_keys[0]
            print("Discard: {}".format(first_key))
            del self.cache_data[first_key]

    def get(self, key):
        """gets the item of the key requested"""
        try:
            if key is None:
                return None
            return self.cache_data[key]
        except KeyError:
            return None
