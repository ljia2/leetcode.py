"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4


Note that both put/get are least recent usage.

1) O(1) Get by random key -> hashtable key, pointer to the entry in linked list
2) O(1) Put:
  2.1) O(1) remove the last entry (invalidate) -> dual linklist
  2.2) O(1) put any entry to front -> dual-linked list


"""
class DualLinkNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict() # key to address of its linked node
        self.recency_head = None # pointing to the head of dual linked list
        self.recency_tail = None # pointing to the tail of dual linked list (least recently used)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache.keys():
            node = self.cache[key]

            # if the node is the last entry, move tail pointer back node if exists
            if node is self.recency_tail and node.prev:
                self.recency_tail = node.prev

            # move this node to the front if it is not already in the front
            if node is not self.recency_head:
                if node.prev:
                    node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                if self.recency_head:
                    node.next = self.recency_head
                    self.recency_head.prev = node
                node.prev = None
                self.recency_head = node

            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache.keys():
            node = self.cache[key]
            # update the new value
            node.val = value

            # if the node is the last entry, move tail pointer back node if exists
            if node is self.recency_tail and node.prev:
                self.recency_tail = node.prev

            if node is not self.recency_head:
                # move this node to the front
                if node.prev:
                    node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                if self.recency_head:
                    node.next = self.recency_head
                    self.recency_head.prev = node
                node.prev = None
                self.recency_head = node
        else:
            if len(self.cache) < self.capacity:
                node = DualLinkNode(key, value)
                # directly put the new node in the front
                if self.recency_head:
                    node.next = self.recency_head
                    self.recency_head.prev = node
                self.recency_head = node
                if not self.recency_tail:
                    self.recency_tail = node
                self.cache[key] = node
            else:
                # note that remove the last node and update the map.
                del self.cache[self.recency_tail.key]
                if self.recency_tail.prev:
                    self.recency_tail.prev.next = None
                self.recency_tail = self.recency_tail.prev

                # put the new node in the front
                node = DualLinkNode(key, value)
                if self.recency_head:
                    node.next = self.recency_head
                    self.recency_head.prev = node
                self.recency_head = node
                if not self.recency_tail:
                    self.recency_tail = node
                self.cache[key] = node
        return


# Your LRUCache object will be instantiated and called as such:
#obj = LRUCache(2)
#print(obj.put(2, 1))
#print(obj.put(2, 2))
#print(obj.get(2))
#print(obj.put(1, 1))
#print(obj.put(4, 1))
#print(obj.get(2))

obj = LRUCache(2)
print(obj.put(1, 1))
print(obj.put(2, 2))
print(obj.get(1))
print(obj.put(3, 3))
print(obj.get(2))
print(obj.put(4, 4))
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))


