from heapq import heappop, heappush


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Given a binary tree, return the vertical order traversal of its nodes values.

    For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

    Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes,
    we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

    If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

    Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.



    Example 1:



    Input: [3,9,20,null,null,15,7]
    Output: [[9],[3,15],[20],[7]]
    Explanation:
    Without loss of generality, we can assume the root node is at position (0, 0):
    Then, the node with value 9 occurs at position (-1, -1);
    The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
    The node with value 20 occurs at position (1, -1);
    The node with value 7 occurs at position (2, -2).
    Example 2:



    Input: [1,2,3,4,5,6,7]
    Output: [[4],[2],[1,5,6],[3],[7]]
    Explanation:
    The node with value 5 and the node with value 6 have the same position according to the given scheme.
    However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.


    Note:

    The tree will have between 1 and 1000 nodes.
    Each node's value will be between 0 and 1000.


    T: O(nlogn)
    S: O(n)
    """
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        # use dfs to record each node's coordinates and value.
        nodehp = []
        self.dfs(root, nodehp, 0, 0)

        # iterate the heap to print vertical lines.
        ans = []
        while nodehp:
            cur_line = []
            x, y, val = heappop(nodehp)
            cur_line.append(val)
            while nodehp:
                nx, ny, nval = heappop(nodehp)
                if nx == x:
                    cur_line.append(nval)
                else:
                    # push back the new val and break
                    heappush(nodehp, (nx, ny, nval))
                    break
            ans.append(cur_line)
        return ans

    def dfs(self, root, hq, x, y):
        heappush(hq, (x, -y, root.val))
        if root.left:
            self.dfs(root.left, hq, x-1, y-1)
        if root.right:
            self.dfs(root.right, hq, x+1, y-1)
        return
