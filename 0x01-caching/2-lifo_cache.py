#!/usr/bin/env python3
"""
Caching Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines:
      - Caching system
    """
    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            least_item = (list(iter(self.cache_data.keys()))).pop(-1)
            print("DISCARD: {}".format(least_item))
            del self.cache_data[least_item]
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
