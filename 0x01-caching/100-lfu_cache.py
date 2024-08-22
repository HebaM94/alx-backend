#!/usr/bin/env python3
"""
Caching Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - Caching system
    """
    def __init__(self):
        """ Initializes new instance
        """
        super().__init__()
        self.counter = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.counter[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                items = list(self.counter.values())
                min_item = min(items)
                least_frequent = [k for k, v in self.counter.items()
                                  if v == min_item]
                least_item = list(iter(least_frequent)).pop(0)
                print("DISCARD: {}".format(least_item))
                del self.cache_data[least_item]
                del self.counter[least_item]
        self.cache_data[key] = item
        self.counter[key] = 1

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        self.counter[key] += 1
        return self.cache_data[key]
