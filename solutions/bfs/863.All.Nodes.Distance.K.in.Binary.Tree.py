from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root, target, K):
        """
        We are given a binary tree (with root node root), a target node, and an integer value K.

        Return a list of the values of all nodes that have a distance K from the target node.
        The answer can be returned in any order.

        Example 1:
        Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
        Output: [7,4,1]

        Explanation:
        The nodes that are a distance 2 from the target node (with value 5)
        have values 7, 4, and 1.

        Note that the inputs "root" and "target" are actually TreeNodes.
        The descriptions of the inputs above are just serializations of these objects.

        Note:

        The given tree is non-empty.
        Each node in the tree has unique values 0 <= node.val <= 500.
        The target node is a node in the tree.
        0 <= K <= 1000.

        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]

        first, convert directed tree to undirected graph.
        second, conduct bfs starting from target
        """

        graph = defaultdict(list)
        self.dfs(root, graph)

        qe = [target]
        visited = set()
        visited.add(target)
        moves = 0

        while qe:
            size = len(qe)
            while size > 0:
                node = qe.pop(0)
                size -= 1

                if moves == K:
                    return list(map(lambda x:x.val, qe))

                if node not in graph.keys():
                    continue

                for dst in graph[node]:
                    if dst in visited:
                        continue
                    qe.append(dst)
                    visited.add(dst)
            moves += 1
        return []

    def dfs(self, root, graph):
        if not root:
            return
        if root.left:
            graph[root].append(root.left)
            graph[root.left].append(root)
            self.dfs(root.left, graph)
        if root.right:
            graph[root].append(root.right)
            graph[root.right].append(root)
            self.dfs(root.right, graph)
        return

# r3 = TreeNode(3)
# r5 = TreeNode(5)
# r1 = TreeNode(1)
# r3.left = r5
# r3.right = r1
# r6 = TreeNode(0)
# r2 = TreeNode(2)
# r5.left = r6
# r5.right = r2
# r7 = TreeNode(7)
# r4 = TreeNode(4)
# r2.left = r7
# r2.right = r4
# r0 = TreeNode(0)
# r8 = TreeNode(8)
# r1.left = r0
# r1.right = r8

r0 = TreeNode(0)
r1 = TreeNode(1)
r0.left = r1
r3 = TreeNode(3)
r2 = TreeNode(2)
r1.left = r3
r1.right = r2

s = Solution()
print(s.distanceK(r0, r2, 1))