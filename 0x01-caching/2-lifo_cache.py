#!/usr/bin/env python3
"""implementin basic caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache class"""

    def __init__(self):
        """initialiser"""
        super().__init__()
        self.last_in = None

    def put(self, key, item):
        """sets keys to item
        and saves to cache data"""
        if key is None or item is None:
            pass
        try:
            initial_vacancy_checked = self.cache_data[key]
        except KeyError:
            initial_vacancy_checked = None
        self.cache_data[key] = item

        if len(self.cache_data) == self.MAX_ITEMS:
            # will only set last_in at replacement or first set of
            # input where length of cached_data == max_items
            # store last in
            self.last_in = key
        # if cache data has more than max items --
        # implementation of last in last out if new key was added
        if len(self.cache_data) > self.\
                MAX_ITEMS and initial_vacancy_checked is None:
            print("Discard: {}".format(self.last_in))
            # delete the key that was the last before
            # the increase from MAX_ITEMS
            del self.cache_data[self.last_in]
        # if key was simply replaced, store it as last in for future reference
        self.last_in = key

    def get(self, key):
        """gets the item of the key requested"""
        try:
            if key is None:
                return None
            return self.cache_data[key]
        except KeyError:
            return None
