from heapq import heapify, heappop

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class DFSSolution(object):
    def verticalOrder(self, root):
        """
        Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

        If two nodes are in the same row and column, the order should be from left to right.

        Examples 1:

        Input: [3,9,20,null,null,15,7]

           3
          /\
         /  \
         9  20
            /\
           /  \
          15   7

        Output:

        [
          [9],
          [3,15],
          [20],
          [7]
        ]
        Examples 2:

        Input: [3,9,8,4,0,1,7]

             3
            /\
           /  \
           9   8
          /\  /\
         /  \/  \
         4  01   7

        Output:

        [
          [4],
          [9],
          [3,0,1],
          [8],
          [7]
        ]
        Examples 3:

        Input: [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5)

             3
            /\
           /  \
           9   8
          /\  /\
         /  \/  \
         4  01   7
            /\
           /  \
           5   2

        Output:

        [
          [4],
          [9,5],
          [3,0,1],
          [8,2],
          [7]
        ]
        :type root: TreeNode
        :rtype: List[List[int]]

        if root is (0, 0):
            root.left is (-1, 1) and root.right is (1, 1)
        use a heap to store a tuple of (x, y, priority, node).

        """

        if not root:
            return []
        # nodes stores tuple of (x, y, order, value)
        nodes = []
        self.dfs(root, 0, 0, nodes)

        heap = heapify(nodes)

        answers = []
        answer = []
        last_x = None
        while heap:
            x, _, _, v = heappop(heap)
            if not answer:
                answer = [v]
                last_x = x
            else:
                if x != last_x:
                    answers.append(answer)
                    answer = [v]
                else:
                    answer.append(v)
                last_x = x

        # IMPORTANT!! DO NOT FORGET THE LAST ANSWER itsef as a list.
        answers.append(answer)
        return answers

    def dfs(self, root, x, y, nodes):
        if not root:
            return
        # tuple of (coordinate, order of in the heap, val).
        nodes.append((x, y, len(nodes), root.val))
        self.dfs(root.left, x-1, y+1, nodes)
        self.dfs(root.right, x+1, y+1, nodes)
        return

