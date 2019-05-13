"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""
import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num2pos = dict()
        self.numloc = []
        self.random = random

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.num2pos.keys():
            return False

        pos = len(self.numloc)
        self.num2pos[val] = pos
        self.numloc.append(val)
        return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.num2pos.keys():
            return False

        pos = self.num2pos[val]
        # swap the last location number with the number w/remove.
        if pos < len(self.numloc) - 1:
            lnum = self.numloc[-1]
            self.numloc[pos] = lnum
            self.num2pos[lnum] = pos

        self.num2pos.pop(val)
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



# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.insert(2)
param_4 = obj.getRandom()
param_5 = obj.remove(1)
param_6 = obj.insert(2)
param_7 = obj.getRandom()