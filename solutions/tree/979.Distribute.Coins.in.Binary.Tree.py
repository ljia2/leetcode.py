# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distributeCoins(self, root):
        """
        Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

        In one move, we may choose two adjacent nodes and move one coin from one node to another.
        (The move may be from parent to child, or from child to parent.)

        Return the number of moves required to make every node have exactly one coin.

        Example 1:
        Input: [3,0,0]
        Output: 2
        Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

        Example 2:
        Input: [0,3,0]
        Output: 3
        Explanation: From the left child of the root, we move two coins to the root [taking two moves].
        Then, we move one coin from the root of the tree to the right child.

        Example 3:
        Input: [1,0,2]
        Output: 2

        Example 4:
        Input: [1,0,0,null,3]
        Output: 4


        Note:
        1<= N <= 100
        0 <= node.val <= N

        https://leetcode.com/problems/distribute-coins-in-binary-tree/description/

        :type root: TreeNode
        :rtype: int

        calculate the flow on each edge of tree.

        give an root with a left and right tree.

        the balance value of root is 1) zero: coins are balanced one per node
                                     2) positive (more coins than one per node)
                                     3) negative (less coins than one per node)

        balance(root) = root.val - 1 + balance(left) + balance(right)

        for left-root and right-root edges: there are abs(balance(left)) moves and abs(balance(right)) moves needed.

        ans += abs(balance(left)) + abs(balance(right))

        """

        if not root:
            return 0

        ans = [0]
        _ = self.balance(root, ans)
        return ans[0]

    # return the positive number of extra coins or the negative number of needed coins.
    def balance(self, root, ans):
        if not root:
            return 0
        left_bal = self.balance(root.left, ans) if root.left else 0
        right_bal = self.balance(root.right, ans) if root.right else 0
        ans[0] += abs(left_bal) + abs(right_bal)
        return root.val - 1 + left_bal + right_bal

