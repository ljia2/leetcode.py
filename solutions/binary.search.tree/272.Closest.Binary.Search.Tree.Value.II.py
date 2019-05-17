# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import heapq
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

        Note:

        Given target value is a floating point.
        You may assume k is always valid, that is: k ≤ total nodes.
        You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

        Example:

        Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

            4
           / \
          2   5
         / \
        1   3

        Output: [4,3]
        Follow up:
        Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
        
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """

        if not root or k == 0:
            return None

        ans = []
        self.dfs(root, target, k, ans)
        return list(map(lambda x: x[1], ans))

    def dfs(self, root, target, k, ans):
        if not root:
            return
        self.pushKHeap(root.val, target, ans, k)
        self.dfs(root.left, target, k, ans)
        self.dfs(root.right, target, k, ans)
        return

    def pushKHeap(self, val, target, ans, k):
        heapq.heappush(ans, (-abs(val-target), val))
        if len(ans) > k:
            heapq.heappop(ans)
        return

### Follow up: Assume that the BST is balanced,
### Could you solve it in less than O(n) runtime (where n = total nodes)?

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

        Note:

        Given target value is a floating point.
        You may assume k is always valid, that is: k ≤ total nodes.
        You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

        Example:

        Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

            4
           / \
          2   5
         / \
        1   3

        Output: [4,3]
        Follow up:
        Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """

        if not root or k <= 0:
            return None

        # store all node whose values smaller than target
        pred = []
        # store all nodes whose values bigger than target
        succ = []

        curr = root
        while curr:
            if target <= curr.val:
                succ.append(curr)
                curr = curr.left
            else:
                pred.append(curr)
                curr = curr.right

        ans = []
        while k > 0:
            if not pred and not succ:
                break
            elif not pred:
                ans.append(self.getSuccessor(succ))
            elif not succ:
                ans.append(self.getPredecessor(pred))
            elif abs(pred[-1].val - target) < abs(succ[-1].val - target):
                ans.append(self.getPredecessor(pred))
            else:
                ans.append(self.getSuccessor(succ))
            k -= 1
        return ans

    # find the predecessor of stack top
    def getPredecessor(self, stack):
        res = stack.pop()
        # find the biggest node whose value < stack top
        curr = res.left
        while curr:
            stack.append(curr)
            curr = curr.right
        return res.val

    def getSuccessor(self, stack):
        res = stack.pop()
        # find the smaller node whose value > stack top.
        curr = res.right
        while curr:
            stack.append(curr)
            curr = curr.left
        return res.val

