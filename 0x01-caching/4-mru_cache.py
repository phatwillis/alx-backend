#!/usr/bin/env python3
"""implementin basic caching"""
import datetime

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Cache class"""

    def __init__(self):
        """initialiser"""
        super().__init__()
        self.cache_data_ages = {}

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
        self.cache_data_ages[key] = datetime.datetime.now()
        cache_ages = {}
        # if cache data has more than max items --
        # implement last recently used if new key is added
        if len(self.cache_data) > self. \
                MAX_ITEMS and initial_vacancy_checked is None:
            for k, v in self.cache_data_ages.items():
                # create a separate dictionary for iteration
                # this separate dict will never have the newly put
                # in key's age because we don't want to remove new inputs
                # upon input.
                if k != key:
                    cache_ages[k] = v
            ages_list = [age for age in cache_ages.values()]
            most_recent_age = ages_list[0]

            # set least_recent_age
            for i in ages_list:
                # if the datetime obj is newer than i,
                # most_recent_age is re-set
                if most_recent_age < i:
                    most_recent_age = i

            # compare the key that has the age as its own
            for k, v in cache_ages.items():
                if v == most_recent_age:
                    most_recent_used = k

                    # remove the most recently used
                    # remove the age k, v pair to update it
                    del self.cache_data_ages[most_recent_used]

                    print("Discard: {}".format(most_recent_used))

                    del self.cache_data[most_recent_used]
        # if key was simply replaced
        if len(self.cache_data) > self. \
                MAX_ITEMS and initial_vacancy_checked is not None:
            for k, v in self.cache_data_ages.items():
                # create a separate dictionary for iteration
                # this separate dict will never have the newly put
                # in key's age because we don't want to remove new inputs
                # upon input.
                if k != key:
                    cache_ages[k] = v
            ages_list = [age for age in cache_ages.values()]
            most_recent_age = ages_list[0]

            # set least_recent_age
            for i in ages_list:
                # if the datetime obj is newer than i,
                # most_recent_age is re-set
                if most_recent_age < i:
                    most_recent_age = i

            # compare the key that has the age as its own
            for k, v in cache_ages.items():
                if v == most_recent_age:
                    most_recent_used = k

                    # remove the most recently used
                    # remove the age k, v pair to update it
                    del self.cache_data_ages[most_recent_used]
                    # remove most recently used
                    del self.cache_data[most_recent_used]

    def get(self, key):
        """gets the item of the key requested"""
        try:
            if key is None:
                return None
            # when a key is used, re-set its use time
            if self.cache_data[key] is not None:
                self.cache_data_ages[key] = datetime.datetime.now()
            return self.cache_data[key]
        except KeyError:
            return None
