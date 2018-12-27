class Solution:
    def shortestPathLength(self, graph):
        """
        An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.
        graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.
        Return the length of the shortest path that visits every node. You may start and stop at any node,
        you may revisit nodes multiple times, and you may reuse edges.


        Example 1:
        Input: [[1,2,3],[0],[0],[0]]
        Output: 4
        Explanation: One possible path is [1,0,2,0,3]

        Example 2:
        Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
        Output: 4
        Explanation: One possible path is [0,1,4,2,3]


        Note:

        1 <= graph.length <= 12
        0 <= graph[i].length < graph.length
        :type graph: List[List[int]]
        :rtype: int

        Again shortest moves via bfs with revisit node (states is (r, c, nodes visisted already))
        see Leetcode 864
        """
        # binary representation of indicating all nodes are visited.
        ans = (1 << len(graph)) - 1
        # typical template for bfs
        qe = []
        visited = set()
        for i in range(len(graph)):
            qe.append((i, 1 << i))
            visited.add((i, 1 << i))
        moves = 0
        while qe:
            size = len(qe)
            while size > 0:
                size -= 1
                # queue: FIFO
                n, vnodes = qe.pop(0)
                if vnodes == ans:
                    return moves
                neighbors = graph[n]
                for neighbor in neighbors:
                    nvnodes = (vnodes | 1 << neighbor)
                    if (neighbor, nvnodes) in visited:
                        continue
                    qe.append((neighbor, nvnodes))
                    visited.add((neighbor, nvnodes))
            moves += 1
        return -1


s = Solution()
print(s.shortestPathLength([[1,2,3],[0],[0],[0]]))