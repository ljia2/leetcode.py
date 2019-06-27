# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Codec:
#     def __init__(self):
#         self.p = re.compile(r"^\[([0-9]+)\,([0-9]+)\,([0-9]+)\](.*?)$")
#
#     def serialize(self, root):
#         """Encodes a tree to a single string.
#
#         :type root: TreeNode
#         :rtype: str
#         """
#         if not root:
#             return ""
#         lcode = self.serialize(root.left)
#         rcode = self.serialize(root.right)
#         offsets = [len(str(root.val)), len(lcode), len(rcode)]
#         return "[" + ",".join(map(lambda x:str(x), offsets)) + "]" + str(root.val) + str(lcode) + str(rcode)
#
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
#         :type data: str
#         :rtype: TreeNode
#         """
#         if not data:
#             return None
#
#         v, l, r, code = self.p.search(data).groups()
#         voffset, loffset, roffset = int(v), int(l), int(r)
#         root = TreeNode(code[:voffset])
#         if loffset > 0:
#             root.left = self.deserialize(code[voffset:voffset+loffset])
#         if roffset > 0:
#             root.right = self.deserialize(code[voffset+loffset:voffset+loffset+roffset])
#         return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

"""
Recursive preorder encode/decode

space O(2n+1) where n is # of nodes. 
"""
class CodecII:
    def serialize(self, root):
        vals = []
        self.encode(root, vals)
        return ' '.join(vals)

    def encode(self, node, vals):
        if not node:
            vals.append("#")
            return
        vals.append(node.val)
        self.encode(node.left, vals)
        self.encode(node.right, vals)
        return

    def deserialize(self, data):
        return self.decode(iter(data.split()))

    def decode(self, val_iter):
        val = next(val_iter)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = self.decode(val_iter)
        node.right = self.decode(val_iter)
        return node


#### Follow up: How about N-ary Tree: LC428
#### use val|size-of-children to denote node and DFS.


