# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Given the root of a binary tree, each node has a value from 0 to 25 representing the letters 'a' to 'z':
    a value of 0 represents 'a', a value of 1 represents 'b', and so on.

    Find the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

    (As a reminder, any shorter prefix of a string is lexicographically smaller: for example, "ab" is lexicographically smaller than "aba".
    A leaf of a node is a node that has no children.)



    Example 1:



    Input: [0,1,2,3,4,3,4]
    Output: "dba"
    Example 2:



    Input: [25,1,3,1,3,0,2]
    Output: "adz"
    Example 3:



    Input: [2,2,1,null,1,0,null,0]
    Output: "abc"


    Note:

    The number of nodes in the given tree will be between 1 and 1000.
    Each node in the tree will have a value between 0 and 25.
    """
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':
        if not root:
            return None
        ans = [None]
        self.dfs(root, "", ans)
        return ans[0]

    def dfs(self, root, path, ans):
        if not root.left and not root.right:
            # update the answer so far
            self.minStr(root, path, ans)
            return
        curr_path = chr(ord('a') + root.val) + path
        if root.left:
            self.dfs(root.left, curr_path, ans)
        if root.right:
            self.dfs(root.right, curr_path, ans)
        return

    def minStr(self, root, curr_path, ans):
        path = chr(ord('a') + root.val) + curr_path

        if not ans[0]:
            ans[0] = path
        else:
            # You can use ( > , < , <= , <= , == , !=  ) to compare two strings.
            # Python compares string lexicographically i.e using ASCII value of the characters.
            ans[0] = path if path < ans[0] else ans[0]
        return


s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.smallestFromLeaf(root))