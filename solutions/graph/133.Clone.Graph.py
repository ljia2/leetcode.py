# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
        Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.


        Example:


        Input:
        {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

        Explanation:
        Node 1's value is 1, and it has two neighbors: Node 2 and 4.
        Node 2's value is 2, and it has two neighbors: Node 1 and 3.
        Node 3's value is 3, and it has two neighbors: Node 2 and 4.
        Node 4's value is 4, and it has two neighbors: Node 1 and 3.


        Note:
        The number of nodes will be between 1 and 100.
        The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
        Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
        You must return the copy of the given node as a reference to the cloned graph.

        :type node: Node
        :rtype: Node

        DFS + dict key = original node, val = copy node.

        """

        if not node:
            return None

        node2copy = dict()
        visited = set()
        self.dfs(node, visited, node2copy)

        return node2copy[node]

    def dfs(self, node, visited, node2copy):
        if node in visited:
            return

        visited.add(node)

        nodecopy = node2copy.get(node, Node(node.val, []))
        node2copy[node] = nodecopy

        for neighbor in node.neighbors:
            neighborcopy = node2copy.get(neighbor, Node(neighbor.val, []))
            node2copy[neighbor] = neighborcopy
            nodecopy.neighbors.append(neighborcopy)
            self.dfs(neighbor, visited, node2copy)
        return

