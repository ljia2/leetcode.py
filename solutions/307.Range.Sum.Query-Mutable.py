# Solution 1 by Segment Tree
"""
Segment tree could be implemented using either an array or a tree.
For an array implementation, if the element at index i is not a leaf, its left and right child are stored at index 2i and 2i + 1 respectively.
"""
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # initialize a segment tree with 2n space where n to 2n-1 stored the original numbers
        self.size = len(nums)
        self.tree = [0] * self.size + nums
        self.buildTree(self.tree)


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        ti = i + self.size
        self.tree[ti] = val
        while ti > 0:
            pti = ti // 2
            if ti % 2 == 0:
                # ti is the left tree of its parent (pti) and ti + 1 is the right tree
                self.tree[pti] = self.tree[ti] + self.tree[ti + 1]
            else:
                # ti is the right tree of its parent (pti) and ti - 1 is the left tree
                self.tree[pti] = self.tree[ti-1] + self.tree[ti]
            ti = pti


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        Note set ti and tj pointing to two leaf nodes.
        1) If ti is the left node and tj is a right node,
        then we can directly move ti = ti // 2 and tj = tj // 2 to find their common parent node (when ti == tj)
        When ti == tj, one of if statements must be executed to update the value of its parent

        2) If ti is not the left node (ti % 2 != 0) but a right node, we update sum with ti's value and move ti += 1 to a left node.
        3) If tj is not a right node (tj % 2 != 1) but a left node, we update sum with tj's value and move tj -= 1 to a right node.


        """
        ti = i + self.size
        tj = j + self.size
        result = 0
        while ti <= tj:
            if ti % 2 != 0:
                result += self.tree[ti]
                ti += 1

            if tj % 2 != 1:
                result += self.tree[tj]
                tj -= 1
            ti //= 2
            tj //= 2
        return result

    def buildTree(self, tree):
        """
        :param tree:
        :return:
        the second half from i + 1 to 2 * len(tree) - 1 storing original numbers; build the tree from 1 to i where tree[i] = tree[2i] + tree[2i+1]
        """
        i = len(tree) // 2 - 1
        while i > 0:
            left = 2*i
            right = 2*i + 1
            tree[i] = tree[left] + tree[right]
            i -= 1


# Your NumArray object will be instantiated and called as such:
obj = NumArray([7,2,7,2,0])
print(obj.sumRange(0, 2))
print(obj.update(1, 2))
print(obj.sumRange(0, 2))