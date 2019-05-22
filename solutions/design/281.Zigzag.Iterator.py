
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.list_index = [0] * 2
        self.next_list_index = 0
        self.lists = [v1, v2]

    def next(self):
        """
        :rtype: int
        """
        result = self.lists[self.next_list_index][self.list_index[self.next_list_index]]
        self.list_index[self.next_list_index] += 1
        self.next_list_index = (self.next_list_index + 1) % 2
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        index = self.list_index[self.next_list_index]
        if index < len(self.lists[self.next_list_index]):
            return True
        else:
            self.next_list_index = (self.next_list_index + 1) % 2
            index = self.list_index[self.next_list_index]
            if index < len(self.lists[self.next_list_index]):
                return True
            else:
                return False



class KZigzagIterator(object):

    def __init__(self, lists):
        """
        Initialize your data structure here.
        :type lists: List[List[Int]
        :type K
        """
        self.K = len(lists)
        self.list_index = [0] * self.K
        self.next_list_index = 0
        self.lists = lists

    def next(self):
        """
        :rtype: int
        """
        result = self.lists[self.next_list_index][self.list_index[self.next_list_index]]
        self.list_index[self.next_list_index] += 1
        self.next_list_index = (self.next_list_index + 1) % self.K
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        index = self.list_index[self.next_list_index]
        while index >= len(self.lists[self.next_list_index]):
            self.next_list_index = (self.next_list_index + 1) % self.K
            index = self.list_index[self.next_list_index]
            if index < len(self.lists[self.next_list_index]):
                return True
        return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())