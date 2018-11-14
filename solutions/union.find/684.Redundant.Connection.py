# from collections import defaultdict
#
# class DFSSolution:
#     def findRedundantConnection(self, edges):
#         """
#         In this problem, a tree is an undirected graph that is connected and has no cycles.
#
#         The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added.
#         The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
#
#         The resulting graph is given as a 2D-array of edges.
#         Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.
#
#         Return an edge that can be removed so that the resulting graph is a tree of N nodes.
#         If there are multiple answers, return the answer that occurs last in the given 2D-array.
#         The answer edge [u, v] should be in the same format, with u < v.
#
#         Example 1:
#         Input: [[1,2], [1,3], [2,3]]
#         Output: [2,3]
#         Explanation: The given undirected graph will be like this:
#           1
#          / \
#         2 - 3
#         Example 2:
#         Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
#         Output: [1,4]
#         Explanation: The given undirected graph will be like this:
#         5 - 1 - 2
#             |   |
#             4 - 3
#
#         Note:
#         The size of the input 2D-array will be between 3 and 1000.
#         Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
#
#         Update (2017-09-26):
#         We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph.
#         For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.
#
#         :type edges: List[List[int]]
#         :rtype: List[int]
#
#         Idea; iterate over edge and build the graph one edge a time. When the s and d in the edge is connected in the graph
#         return that edge; otherwise add the edge into to graph.
#
#         To determine whether two nodes are connected in the graph, we use the deep first search (i.e. recursively call function over neighbors).
#
#         T: O(n^2)
#         S: O(n)
#
#         """
#
#         graph = defaultdict(list)
#         for edge in edges:
#             s, d = edge
#             # if s and d are connected, then there is a circle by the edge (s, d)
#             visited = []
#             if self.is_connected(graph, s, d, visited):
#                 return edge
#             # put the edge into the undirected graph
#             graph[s].append(d)
#             graph[d].append(s)
#         return []
#
#     # idea is use recursive call of is_connected by deep first search the graph
#     def is_connected(self, graph, start, end, visited):
#         if start == end:
#             return True
#
#         if start not in graph.keys() or end not in graph.keys():
#             return False
#
#         visited.append(start)
#         destinations = graph[start]
#         for d in destinations:
#             # given a undirected graph, avoid back to visited node to infinite loop
#             if d in visited:
#                 continue
#             if self.is_connected(graph, d, end, visited):
#                 return True
#         return False
#
#
# s = DFSSolution()
# print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))


class UnionFindSolution:
    def findRedundantConnection(self, edges):
        """
        In this problem, a tree is an undirected graph that is connected and has no cycles.

        The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added.
        The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

        The resulting graph is given as a 2D-array of edges.
        Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

        Return an edge that can be removed so that the resulting graph is a tree of N nodes.
        If there are multiple answers, return the answer that occurs last in the given 2D-array.
        The answer edge [u, v] should be in the same format, with u < v.

        Example 1:
        Input: [[1,2], [1,3], [2,3]]
        Output: [2,3]
        Explanation: The given undirected graph will be like this:
          1
         / \
        2 - 3
        Example 2:
        Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
        Output: [1,4]
        Explanation: The given undirected graph will be like this:
        5 - 1 - 2
            |   |
            4 - 3

        Note:
        The size of the input 2D-array will be between 3 and 1000.
        Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

        Update (2017-09-26):
        We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph.
        For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.

        :type edges: List[List[int]]
        :rtype: List[int]

        Union Find Solutions:

        initially, all nodes pointing to themselves and all nodes have the same rank of 1.

        given a edge,
        1) if two nodes are pointint to the same parent, return that edge as the unique Redundant edge.
        2) Otherwise, find their parent (path compression in find) and union by ranks.




        """
        # assuming n edges are not connected
        # note initialize n + 1 for convenience, directly use node (int) as index
        # all nodes pointing to node 0 as parent
        parents = [i for i in range(len(edges) + 1)]

        # ranks representing the size of connected components, initially assuming one edge per component
        ranks = [1 for i in range(len(edges) + 1)]

        for edge in edges:
            s, d = edge

            # find their parents
            ps = self.find(s, parents)
            pd = self.find(d, parents)

            # if ps == pd, s and d pointing to the same parent and thus they are connected
            if ps == pd:
                return edge

            if ranks[ps] > ranks[pd]:
                ps, pd = pd, ps

            # the small component pointing to the large component by updating parent of ps
            parents[ps] = pd
            # update pd's size with ps
            ranks[pd] += ranks[ps]
        return []

    # a classic method of find method for union find
    def find(self, s, parents):
        while parents[s] != s:
            # updating parent of s to its grandparents
            parents[s] = parents[parents[s]]
            # then search from the grandparent
            s = parents[s]
        return s

s = UnionFindSolution()
print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))