"""
Serialization is the process of converting a data structure or object into a sequence of bits
so that it can be stored in a file or memory buffer, or transmitted across a network connection
link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree.
An N-ary tree is a rooted tree in which each node has no more than N children.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree


as [1 [3[5 6] 2 4]]. You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.


Recursive preorder encode/decode

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        vals = []
        self.encode(root, vals)
        return " ".join(vals)

    def encode(self, root, vals):
        if not root:
            return vals.append("#")

        val = str(root.val)
        size = len(root.children)
        vals.append(val + "|" + str(size))
        if size > 0:
            for child in root.children:
                self.encode(child, vals)
        return

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        vals = data.split(" ")
        return self.decode(iter(vals))

    def decode(self, val_iter):
        val_str = next(val_iter)
        if val_str == "#":
            return None

        val, size = val_str.split("|")
        val = int(val)
        size = int(size)
        children = []
        while size > 0:
            size -= 1
            children.append(self.decode(val_iter))
        return Node(val, children)



# Your Codec object will be instantiated and called as such:
codec = Codec()
root = Node(1, [])
root.children.extend([Node(3, [Node(5, []), Node(6, [])]), Node(2, []), Node(4, [])])
code = codec.serialize(root)
print(code)
root2 = codec.deserialize(code)
print(codec.serialize(root2))
print = codec.serialize(None)