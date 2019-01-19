from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def reachableNodes(self, edges, M, N):
        """
        Starting with an undirected graph (the "original graph") with nodes from 0 to N-1, subdivisions are made to some of the edges.

        The graph is given as follows: edges[k] is a list of integer pairs (i, j, n) such that (i, j) is an edge of the original graph,

        and n is the total number of new nodes on that edge.

        Then, the edge (i, j) is deleted from the original graph, n new nodes (x_1, x_2, ..., x_n) are added to the original graph,

        and n+1 new edges (i, x_1), (x_1, x_2), (x_2, x_3), ..., (x_{n-1}, x_n), (x_n, j) are added to the original graph.

        Now, you start at node 0 from the original graph, and in each move, you travel along one edge.

        Return how many nodes you can reach in at most M moves.



        Example 1:

        Input: edges = [[0,1,10],[0,2,1],[1,2,2]], M = 6, N = 3
        Output: 13
        Explanation:
        The nodes that are reachable in the final graph after M = 6 moves are indicated below.

        Example 2:

        Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], M = 10, N = 4
        Output: 23


        Note:

        0 <= edges.length <= 10000
        0 <= edges[i][0] < edges[i][1] < N
        There does not exist any i != j for which edges[i][0] == edges[j][0] and edges[i][1] == edges[j][1].
        The original graph has no parallel edges.
        0 <= edges[i][2] <= 10000
        0 <= M <= 10^9
        1 <= N <= 3000
        A reachable node is a node that can be travelled to using at most M moves starting from node 0.

        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int

        M hints the algorithm can only depend on edges.length and/or N.

        weights (# moves) of edges u, v = # nodes + 1
        BFS with the weight calculation seems to be the method. However, when expansion based on original edge.

        when u to v is not expanded due to insufficent remaining weights, # nodes = min(w_u, # nodes between u and v).

        """

        # establish the graph
        graph = defaultdict(list)
        weight = dict()
        for edge in edges:
            s, d, e = edge
            graph[s].append(d)
            graph[d].append(s)
            weight[(s, d)] = e + 1
            weight[(d, s)] = e + 1

        if 0 not in graph.keys():
            return 1

        # now weighted_bfs over graph !!!

        pq = [] # use as a max pq to store <# moves, node>
        node2move = dict()
        heappush(pq, (-M, 0)) # use negative moves for max queue
        # while pq is not empty
        while pq:
            moves, node = heappop(pq)
            moves = - moves
            if node in node2move.keys():
                continue
            node2move[node] = moves
            for dnode in graph[node]:
                remaining_moves = moves - weight[(node, dnode)]
                if dnode in node2move.keys() or remaining_moves < 0:
                    continue
                heappush(pq, (-remaining_moves, dnode))

        ans = len(node2move.keys())
        for edge in edges:
            s, d, e = edge
            ws = node2move.get(s, 0)
            wd = node2move.get(d, 0)
            # here is the trick:
            # when partially traverse the edge, the visited nodes is ws + wd
            # when fully traverse the edge, ws + wd >= e, the visited nodes is e
            ans += min(e, ws + wd)
        return ans

s = Solution()
print(s.reachableNodes([[0,1,10],[0,2,1],[1,2,2]], 6, 3))
#print(s.reachableNodes([[1, 2, 5], [0, 3, 3], [1, 3, 2], [2, 3, 4], [0, 4, 1]], 7, 5))

