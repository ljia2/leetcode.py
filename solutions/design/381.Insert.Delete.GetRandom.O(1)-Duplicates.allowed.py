"""
Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();

"""
import random
from collections import defaultdict

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num2freq = dict()
        self.num2pos = defaultdict(list)
        self.numloc = []
        self.random = random

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        pos = len(self.numloc)
        self.num2pos[val].append(pos)
        self.numloc.append(val)
        self.num2freq[val] = self.num2freq.get(val, 0) + 1
        return True if self.num2freq[val] == 1 else False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.num2pos.keys() or not self.num2pos[val]:
            return False

        pos = self.num2pos[val].pop()
        # swap the last location number with the number w/remove.
        if pos < len(self.numloc) - 1:
            lnum = self.numloc[-1]
            self.numloc[pos] = lnum
            self.num2pos[lnum].add(pos)
            self.num2freq[val] -= 1

        if self.num2freq[val] == 0:
            self.num2pos.pop(val)
            self.num2freq.pop(val)

        self.numloc.pop()
        return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        # note that randint(a, b) to pick a random integer a<=random<=b.
        ri = self.random.randint(0, len(self.numloc) - 1)
        return self.numloc[ri]




# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.insert(2)
param_4 = obj.getRandom()
param_5 = obj.remove(1)
param_6 = obj.insert(2)
param_7 = obj.getRandom()