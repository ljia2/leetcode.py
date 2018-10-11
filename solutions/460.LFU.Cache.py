from collections import defaultdict, OrderedDict
"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity,
it should invalidate the least frequently used item before inserting a new item.
For the purpose of this problem, when there is a tie
(i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4


"""
class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        # key, freq pair
        self.key2freq = dict()
        # key, ordereddict pair where ordereddict stores (key, value)
        self.freq2recency = defaultdict(OrderedDict)
        # indicate the minimum Frequency stored in cache
        self.minFreq = 2**31

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.capacity == 0:
            return -1

        if key in self.key2freq.keys():
            ofreq = self.key2freq[key]
            nfreq = ofreq + 1

            # update key2freq dictionary
            self.key2freq[key] = nfreq

            # del (key, value, ofreq) from freq2recency
            odict = self.freq2recency[ofreq]
            value = odict[key]
            odict.pop(key)
            # if key is the only element with ofreq, pop ofreq from freq2recency
            if not odict:
                self.freq2recency.pop(ofreq)

            # put (key, value, nfreq) into freq2recency
            odict = self.freq2recency.get(nfreq, OrderedDict())
            odict[key] = value
            self.freq2recency[nfreq] = odict

            if self.minFreq == ofreq:
                if ofreq not in self.freq2recency.keys():
                    self.minFreq = nfreq
            return value
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return

        ofreq = self.key2freq.get(key, 0)
        nfreq = ofreq + 1
        self.key2freq[key] = nfreq

        # we need to pop first and then insert the new key into cache
        if len(self.key2freq) > self.capacity:
            # pop the least recent item
            k, v = self.freq2recency[self.minFreq].popitem(last=False)
            self.key2freq.pop(k)

        # update minFreq if key is new, then it frequency must be minimum
        if self.minFreq > nfreq:
            self.minFreq = nfreq

        # update freq2recency for existing key
        if ofreq in self.freq2recency.keys():
            odict = self.freq2recency[ofreq]
            odict.pop(key)
            if not odict:
                self.freq2recency.pop(ofreq)
                # if the key is the only existing with minimum frequency, update minimue frequency 
                if self.minFreq == ofreq:
                    self.minFreq = nfreq

        # update freq2recency for key
        odict = self.freq2recency.get(nfreq, OrderedDict())
        odict[key] = value
        self.freq2recency[nfreq] = odict

        return




# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(2)
print(obj.put(1, 1))
print(obj.put(2, 2))
print(obj.get(1))
print(obj.put(3, 3))
print(obj.get(2))
print(obj.get(3))
print(obj.put(4, 4))
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))