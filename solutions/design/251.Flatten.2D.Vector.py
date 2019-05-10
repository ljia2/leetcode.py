"""
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.



Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false


Notes:

Please remember to RESET your class variables declared in Vector2D, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume that next() call will always be valid, that is, there will be at least a next element in the 2d vector when next() is called.
"""
class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.stack = [[v, 0]]

    def next(self):
        """
        :rtype: int
        """
        ans = None
        if self.hasNext():
            v, i = self.stack[-1]
            ans = v[i]
            self.stack[-1][1] += 1
        return ans

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            v, i = self.stack[-1]
            if i == len(v):
                self.stack.pop()
            else:
                if type(v[i]) == list:
                    self.stack[-1][1] += 1
                    self.stack.append([v[i], 0])
                else:
                    return True
        return bool(self.stack)

# Your Vector2D object will be instantiated and called as such:
obj = Vector2D([[1,2], [3], [4]])
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())