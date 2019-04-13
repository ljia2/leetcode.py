"""
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled,
and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.


Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]

Note:

The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000.


完全二叉树是每一层都满的，因此找出要插入节点的父亲节点是很简单的。如果用数组tree保存着所有节点的层次遍历，那么新节点的父亲节点就是tree[(N -1)/2]，N是未插入该节点前的树的元素个数。

构建树的时候使用层次遍历，也就是BFS把所有的节点放入到tree里。插入的时候直接计算出新节点的父亲节点。获取root就是数组中的第0个节点。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = []
        # bfs to initialize self.nodes
        q = []
        while q:
            n = q.pop(0)
            self.nodes.append(n)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)
        l = len(self.nodes)
        pindex = (l-1)//2
        if self.nodes[pindex].left:
            self.nodes[pindex].right = node
        else:
            self.nodes[pindex].left = node
        self.nodes.append(node)
        return self.nodes[pindex].val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.nodes[0]


root = TreeNode(1)
s = CBTInserter(root)
s.insert(2)
print(s.get_root())
