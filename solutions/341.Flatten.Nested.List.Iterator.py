# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.num_queue = []
        self.list_stack = []
        if nestedList:
            for nl in nestedList:
                if nl.isInteger():
                    self.num_queue.append(nl.getInteger())
                else:
                    self.list_stack.append((nl.getList(), 0))
                    # exhaust the list_stack to put all nums into queue
                    while self.list_stack:
                        # process next list
                        (l, i) = self.list_stack.pop()
                        while l and i < len(l):
                            if l[i].isInteger():
                                self.num_queue.append(l[i].getInteger())
                                i += 1
                            else:
                                self.list_stack.append((l, i + 1))
                                self.list_stack.append((l[i].getList(), 0))
                                break

    def next(self):
        """
        :rtype: int
        """
        top_num = self.num_queue[0]
        self.num_queue = self.num_queue[1:]
        return top_num

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.num_queue:
            return True
        else:
            return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())