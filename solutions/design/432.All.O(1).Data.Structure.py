"""
Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.

"""
class KVNode:
    def __init__(self, val):
        self.val = val
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # key -> KVNode in linkedlist
        self.keydict = dict()
        self.head = None
        self.tail = None

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """

        if key not in self.keydict.keys():
            if not self.head and not self.tail:
                node = KVNode(1)
                node.keys.add(key)
                self.head = node
                self.tail = node
            elif self.head.val != 1:
                node = KVNode(1)
                node.keys.add(key)
                self.head.prev = node
                node.next = self.head
                self.head = node
            else:
                self.head.keys.add(key)

            self.keydict[key] = self.head
            return

        node = self.keydict[key]
        if self.head == node and self.tail == node:
            node.keys.remove(key)
            if not node.keys:
                self.tail = None
                self.head = None

            nnode = KVNode(node.val + 1)
            nnode.keys.add(key)

            if not self.head:
                self.head = nnode

            if not self.tail:
                self.tail = nnode
            else:
                nnode.prev = self.tail
                self.tail.next = nnode
                self.tail = nnode

            self.keydict[key] = nnode
        elif self.tail == node:
            node.keys.remove(key)
            if not node.keys:
                self.tail = self.tail.prev

            nnode = KVNode(node.val + 1)
            nnode.keys.add(key)
            self.tail.next = nnode
            nnode.prev = self.tail
            self.tail = nnode

            self.keydict[key] = nnode
        elif self.head == node:
            node.keys.remove(key)
            if not node.keys:
                self.head = self.head.next
                self.head.prev = None

            if node.next.val == node.val + 1:
                node.next.keys.add(key)
                self.keydict[key] = node.next
            else:
                nnode = KVNode(node.val + 1)
                nnode.keys.add(key)
                self.head.prev = nnode
                nnode.next = self.head
                self.head = nnode

                self.keydict[key] = nnode
        else:
            prev = node.prev
            succ = node.next
            node.keys.remove(key)
            if not node.keys:
                prev.next = succ
                succ.prev = prev

            if succ.val == node.val + 1:
                succ.keys.add(key)
                self.keydict[key] = succ
            else:
                nnode = KVNode(node.val + 1)
                prev.next = nnode
                nnode.prev = prev
                nnode.next = succ
                succ.prev = nnode
                self.keydict[key] = nnode

        return

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key not in self.keydict.keys():
            return

        node = self.keydict[key]
        if self.head == node and self.tail == node:
            node.keys.remove(key)
            if not node.keys:
                self.head = None
                self.head = None

            if node.val - 1 == 0:
                self.keydict.pop(key)
            else:
                nnode = KVNode(node.val - 1)
                nnode.keys.add(key)
                if not self.head:
                    self.head = nnode
                else:
                    self.head.prev = nnode
                    nnode.next = self.head
                    self.head = nnode

                if not self.tail:
                    self.tail = nnode

                self.keydict[key] = nnode

        elif self.head == node:
            node.keys.remove(key)
            if not node.keys:
                self.head = self.head.next
                self.head.prev = None

            if node.val - 1 == 0:
                self.keydict.pop(key)
            else:
                nnode = KVNode(node.val - 1)
                nnode.keys.add(key)
                self.head.prev = nnode
                nnode.next = self.head
                self.head = nnode

                self.keydict[key] = nnode
        elif self.tail == node:
            node.keys.remove(key)
            if not node.keys:
                self.tail = self.tail.prev
                self.tail.next = None
                if node.val - 1 == 0:
                    self.keydict.pop(key)
                elif self.tail.val == node.val - 1:
                    self.tail.keys.add(key)
                    self.keydict[key] = self.tail
                else:
                    nnode = KVNode(node.val -1)
                    nnode.keys.add(key)
                    self.tail.next = nnode
                    nnode.prev = self.tail
                    self.tail = nnode
                    self.keydict[key] = nnode
            else:
                if node.val - 1 == 0:
                    self.keydict.pop(key)
                elif node.prev.val == node.val - 1:
                    node.prev.keys.add(key)
                    self.keydict[key] = node.prev
                else:
                    prev = node.prev
                    succ = node
                    nnode = KVNode(node.val -1)
                    nnode.keys.add(key)
                    prev.next = nnode
                    nnode.prev = prev
                    succ.prev = nnode
                    nnode.next = succ
                    self.keydict[key] = nnode

        else:
            prev = node.prev
            succ = node.next

            node.keys.remove(key)
            if not node.keys:
                prev.next = succ
                succ.prev = prev

            if node.val - 1 == 0:
                self.keydict.pop(key)
            elif prev.val == node.val - 1:
                prev.keys.add(key)
                self.keydict[key] = prev
            else:
                nnode = KVNode(node.val -1)
                nnode.keys.add(key)
                prev.next = nnode
                nnode.prev = prev
                succ.prev = nnode
                nnode.next = succ
                self.keydict[key] = nnode

        return

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if not self.tail:
            return ""
        else:
            ans = self.tail.keys.pop()
            self.tail.keys.add(ans)
            return ans


    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if not self.head:
            return ""
        else:
            ans = self.head.keys.pop()
            self.head.keys.add(ans)
            return ans



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc("hello")
# obj.inc("hello")
# obj.getMaxKey()
# obj.getMinKey()
# obj.inc("leet")
# obj.getMaxKey()
# obj.getMinKey()



# obj = AllOne()
# obj.inc("hello")
# obj.inc("goodbye")
# obj.inc("hello")
# obj.inc("hello")
# obj.getMaxKey()
# obj.inc("leet")
# obj.inc("code")
# obj.inc("code")
# obj.dec("hello")
# obj.inc("leet")
# obj.inc("code")
# obj.inc("code")
# obj.getMaxKey()
# obj.inc("leet")
# obj.getMaxKey()
# obj.getMinKey()


obj = AllOne()
obj.inc("a")
obj.inc("b")
obj.inc("b")
obj.inc("b")
obj.inc("b")
obj.dec("b")
obj.dec("b")
obj.getMaxKey()
obj.getMinKey()