import re
from utils.TreeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        lcode = self.serialize(root.left)
        rcode = self.serialize(root.right)
        offsets = [len(str(root.val)), len(lcode), len(rcode)]
        return "[" + ",".join(map(lambda x:str(x), offsets)) + "]" + str(root.val) + str(lcode) + str(rcode)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        p = re.compile(r"^\[([0-9]+)\,([0-9]+)\,([0-9]+)\](.*?)$")
        v, l, r, code = p.search(data).groups()
        voffset, loffset, roffset = int(v), int(l), int(r)
        root = TreeNode(code[:voffset])
        if loffset > 0:
            root.left = self.deserialize(code[voffset:voffset+loffset])
        if roffset > 0:
            root.right = self.deserialize(code[voffset+loffset:voffset+loffset+roffset])
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))