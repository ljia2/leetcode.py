# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

        The root is the maximum number in the array.
        The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
        The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
        Construct the maximum tree by the given array and output the root node of this tree.

        Example 1:
        Input: [3,2,1,6,0,5]
        Output: return the tree root node representing the following tree:

              6
            /   \
           3     5
            \    /
             2  0
               \
                1
        Note:
        The size of the given array will be in the range [1,1000].

        :type nums: List[int]
        :rtype: TreeNode


        Time O(n^2)
        Space O(n)

        """
        if not nums:
            return None

        n = len(nums)
        max_index = None
        for i in range(n):
            # not zero is True!!!!
            if max_index is None:
                max_index = i
            elif nums[i] > nums[max_index]:
                max_index = i

        lroot = self.constructMaximumBinaryTree(nums[:max_index])
        rroot = self.constructMaximumBinaryTree(nums[max_index+1:]) if max_index + 1 < n else None

        root = TreeNode(nums[max_index])
        root.left, root.right = lroot, rroot

        return root

s = Solution()
print(s.constructMaximumBinaryTree([3,2,1,6,0,5]))



class LinearSolution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

        The root is the maximum number in the array.
        The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
        The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
        Construct the maximum tree by the given array and output the root node of this tree.

        Example 1:
        Input: [3,2,1,6,0,5]
        Output: return the tree root node representing the following tree:

              6
            /   \
           3     5
            \    /
             2  0
               \
                1
        Note:
        The size of the given array will be in the range [1,1000].

        :type nums: List[int]
        :rtype: TreeNode


        # intuition: because we are traversing from left to right
        # and because from a dividing node standpoint, nodes with value smaller than itself will be on the left (because we have not seen the right values yet!)
        # traverse the list and build the tree along the way
        # keep track a stack, where the bottom of stack is the largest value we have seen
        # so far
        # make sure the numbers in stack is in decreasing order
        # for each new value we see, we make it into a TreeNode
        # if new value is smaller than top of the stack, we push new value in stack
        # append the new treenode to the right of previous TreeNode
        # if new value is greater than top of stack. Keep poping from the stack until the stack is empty or top of stack value is greater than the new value
        # append the last node being poped as the left node of new node

        O(n)
        O(n)
        """
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        # stack store the node in decreasing order.
        # node1.right = node2; node2.right = node3.......
        stack = []
        for num in nums:
            cur = TreeNode(num)
            # find the largest node whose value < num, it should be the left child of cur.
            while stack and stack[-1].val < num:
                cur.left = stack.pop()
            # if stack, the top node must bigger than num
            # cur must be the right child of that top node.
            if stack:
                stack[-1].right = cur
            # push cur into stack.
            stack.append(cur)
        return stack[0]

ls = LinearSolution()
print(ls.constructMaximumBinaryTree([3,2,1,6,0,5]))
