class Solution:
    def isBipartite(self, graph):
        """

        Given an undirected graph, return true if and only if it is bipartite.

        Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B
        such that every edge in the graph has one node in A and another node in B.

        The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.
        Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i,
        and it doesn't contain any element twice.

        Example 1:
        Input: [[1,3], [0,2], [1,3], [0,2]]
        Output: true
        Explanation:
        The graph looks like this:
        0----1
        |    |
        |    |
        3----2
        We can divide the vertices into two groups: {0, 2} and {1, 3}.

        Example 2:
        Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
        Output: false
        Explanation:
        The graph looks like this:
        0----1
        | \  |
        |  \ |
        3----2
        We cannot find a way to divide the set of nodes into two independent subsets.


        Note:

        graph will have length in range [1, 100].
        graph[i] will contain integers in range [0, graph.length - 1].
        graph[i] will not contain i or duplicate values.
        The graph is undirected: if any element j is in graph[i], then i will be in graph[j].


        :type graph: List[List[int]]
        :rtype: bool

        Need to iterate over all node to determine whether each connected component can be represented by bipartiate graph.

        Specifically, use bfs to start expanding an unexplored node and record steps.

        steps % 2 == 0, checking whether new nodes appears in set1
        step2 % 2 == 1, checking whether new nodes appears in set9.

        If so, return False

        Overall exit loop return True

        """

        if not graph or len(graph) <=2:
            return True


        visited = set()
        for node in range(len(graph)):
            if node in visited:
                continue
            qe = [node]
            set0 = set()
            set0.add(node)
            set1 = set()
            steps = 0
            while qe:
                size = len(qe)
                while size > 0:
                    n = qe.pop(0)
                    size -= 1
                    if steps % 2 == 0:
                        if n in set1:
                            return False
                    else:
                        if n in set0:
                            return False

                    for nn in graph[n]:
                        if steps % 2 == 0:
                            if nn in set1:
                                continue
                        else:
                            if nn in set0:
                                continue

                        qe.append(nn)
                        if steps % 2 == 0:
                            set1.add(nn)
                        else:
                            set0.add(nn)
                steps += 1
            visited.union(set0)
            visited.union(set1)
        return True

s = Solution()
print(s.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]]))


