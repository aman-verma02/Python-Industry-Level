## An LRU cache is a data structure that stores a limited number of items and evicts the least recently used item when the cache exceeds its capacity. The LRU cache supports two operations: get and put.
## The get operation retrieves the value of the key if it exists in the cache, otherwise returns -1. The put operation adds a key-value pair to the cache. If the cache exceeds its capacity, it should evict the least recently used item before adding the new item.


'''
❓ Problem
Design a cache with:
fixed capacity
get(key)
put(key, value)
remove least recently used item when full


🧠 Thinking
We need:
Fast lookup → dictionary
Track usage order → list / ordered structure
'''





class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}        # key → value
        self.order = []        # track usage

    def get(self, key):
        if key not in self.cache:
            return -1
        
        # move key to end (recently used)
        self.order.remove(key)
        self.order.append(key)
        
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        
        elif len(self.cache) >= self.capacity:
            # remove least recently used
            lru = self.order.pop(0)
            del self.cache[lru]

        self.cache[key] = value
        self.order.append(key)

'''
⚠ Edge Cases
Access updates priority
Updating existing key
Capacity overflow
'''