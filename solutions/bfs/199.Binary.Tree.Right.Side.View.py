# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BFSSolution:
    def rightSideView(self, root):
        """

        Given a binary tree, imagine yourself standing on the right side of it,
        return the values of the nodes you can see ordered from top to bottom.

        Example:

        Input: [1,2,3,null,5,null,4]
        Output: [1, 3, 4]
        Explanation:

           1            <---
         /   \
        2     3         <---
         \     \
          5     4       <---
        :type root: TreeNode
        :rtype: List[int]

        Tree BFS via queue.

        """
        if not root:
            return []

        view = []
        # mimic queue to execute BFS
        q = [(0, root)]
        while q:
            size = len(q)
            while size > 0:
                l, node = q.pop(0)
                size -= 1

                # a right node is encountered.
                if size == 0:
                    view.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return view


s = BFSSolution()
root = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
root.left, root.right = n2, n3
n4 = TreeNode(4)
n5 = TreeNode(5)
n2.right = n5
n3.right = n4
print(s.rightSideView(root))

## Follow up: how to reduce space complexity? Use DFS
class DFSSolution:
    def rightSideView(self, root):
        """

        Given a binary tree, imagine yourself standing on the right side of it,
        return the values of the nodes you can see ordered from top to bottom.

        Example:

        Input: [1,2,3,null,5,null,4]
        Output: [1, 3, 4]
        Explanation:

           1            <---
         /   \
        2     3         <---
         \     \
          5     4       <---
        :type root: TreeNode
        :rtype: List[int]

        Complexity Analysis

        Time complexity : O(n).

        Because a binary tree with only child pointers is directed acyclic graph with only one source node,
        a traversal of the tree from the root will visit each node exactly once
        (plus a sublinear amount of leaves, represented as None). Each visitation requires only O(1) work,
        so the while loop runs in linear time.

        Finally, building the array of rightmost values is O(O(height of the tree) = O(n))=O(n)
        because it is not possible for a right-hand view of the tree to contain more nodes than the tree itself.

        Space complexity : O(n).

        At worst, our stack will contain a number of nodes close to the height of the tree.
        Because we are exploring the tree in a depth-first order, there are never two nodes from different subtrees of the same parent node on the stack at once.
        Said another way, the entire right subtree of a node will be visited before any nodes of the left subtree are pushed onto the stack.
        If this logic is applied recursively down the tree, it follows that the stack will be largest when we have reached the end of the tree's longest path (the height of the tree). However, because we know nothing about the tree's topography, the height of the tree may be equivalent to nn, causing the space complexity to degrade to O(n)O(n)

        """
        if not root:
            return []

        viewdict = dict()
        # mimic queue to execute BFS
        stack = [(root, 0)]
        max_depth = -1
        while stack:
            node, depth = stack.pop()
            # maintain the level of tree.
            max_depth = max(max_depth, depth)

            if depth not in viewdict.keys():
                viewdict[depth] = node.val

            if node.left:
                stack.append((node.left, depth + 1))

            if node.right:
                stack.append((node.right, depth + 1))

        return [viewdict[k] for k in range(max_depth+1)]



