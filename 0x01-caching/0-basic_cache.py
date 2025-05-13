#!/usr/bin/env python3
"""implementin basic caching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache class"""

    def __init__(self):
        """initialiser"""
        super().__init__()

    def put(self, key, item):
        """sets keys to item
        and saves to cache data"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """gets the item of the key requested"""
        try:
            if key is None:
                return None
            return self.cache_data[key]
        except KeyError:
            return None
