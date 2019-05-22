# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class DFSSolution(object):
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
        self.dfs(node, set(), node2copy)

        return node2copy[node]

    def dfs(self, node, visited, node2copy):
        if node in visited:
            return

        visited.add(node)

        if node not in node2copy.keys():
            node2copy[node] = Node(node.val, [])

        for neighbor in node.neighbors:
            if neighbor not in node2copy.keys():
                neighborcopy = node2copy[neighbor]
            else:
                neighborcopy = Node(neighbor.val, [])
                node2copy[neighbor] = neighborcopy
            node2copy[node].neighbors.append(neighborcopy)
            self.dfs(neighbor, visited, node2copy)
        return


class BFSSolution(object):
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

        BFS + dict key = original node, val = copy node.

        """

        if not node:
            return None

        node2copy = dict()
        self.bfs(node, node2copy)
        return node2copy[node]

    def bfs(self, node, node2copy):
        qe = [node]
        visited = set()
        while qe:
            size = len(qe)
            while size > 0:
                n = qe.pop(0)
                size -= 0

                if n in visited:
                    continue

                # get or generate the copy of node
                node2copy[n] = Node(n.val, [])
                visited.add(n)
                # populate the neighbors of nn according to that of n.
                for neighbor in n.neighbors:
                    qe.append(neighbor)
                # n node's copy nn's neighbor has been populated.

        # set up the dict node2copy by cloning the edges
        for node in node2copy.keys():
            for neighbor in node.neighbors:
                node2copy[node].neighbors.append(node2copy[neighbor])

        return

