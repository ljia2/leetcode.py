from collections import defaultdict


# class DFSSolution: # TLE
#     def canFinish(self, numCourses, prerequisites):
#         """
#         There are a total of n courses you have to take, labeled from 0 to n-1.
#
#         Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
#
#         Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
#         Example 1:
#
#         Input: 2, [[1,0]]
#         Output: true
#         Explanation: There are a total of 2 courses to take.
#                      To take course 1 you should have finished course 0. So it is possible.
#         Example 2:
#
#         Input: 2, [[1,0],[0,1]]
#         Output: false
#         Explanation: There are a total of 2 courses to take.
#                      To take course 1 you should have finished course 0, and to take course 0 you should
#                      also have finished course 1. So it is impossible.
#         Note:
#
#         The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
#         Read more about how a graph is represented.
#         You may assume that there are no duplicate edges in the input prerequisites.
#
#         :type numCourses: int
#         :type prerequisites: List[List[int]]
#         :rtype: bool
#
#         use employ topological sorting to determine whether a directed graph has a circle
#
#         O(n)
#
#         """
#         graph = defaultdict(list)
#         for (c, p) in prerequisites:
#             graph[c].append(p)
#
#         for i in range(numCourses):
#             visited = [i]
#             if self.dfs(graph, i, visited):
#                 return False
#         return True
#
#     # return True when the graph has a circle; False otherwise.
#     def dfs(self, graph, node, visited):
#         if node not in graph.keys():
#             return False
#
#         # dfs for each neighbor
#         for neighbor in graph[node]:
#             if neighbor in visited:
#                 return True
#
#             visited.append(neighbor)
#             if self.dfs(graph, neighbor, visited):
#                 return True
#             visited.remove(neighbor)
#
#         return False


class TopologicalSortingSolution:
    def canFinish(self, numCourses, prerequisites):
        """
        There are a total of n courses you have to take, labeled from 0 to n-1.

        Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

        Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

        Example 1:

        Input: 2, [[1,0]]
        Output: true
        Explanation: There are a total of 2 courses to take.
                     To take course 1 you should have finished course 0. So it is possible.
        Example 2:

        Input: 2, [[1,0],[0,1]]
        Output: false
        Explanation: There are a total of 2 courses to take.
                     To take course 1 you should have finished course 0, and to take course 0 you should
                     also have finished course 1. So it is impossible.
        Note:

        The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
        Read more about how a graph is represented.
        You may assume that there are no duplicate edges in the input prerequisites.

        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        use employ topological sorting to determine whether a directed graph has a circle

        O(V)

        """
        graph = defaultdict(list)
        for (c, p) in prerequisites:
            graph[c].append(p)

        # each node has either visiting or visited status.
        # 0 = unknown, 1 = visiting,  2 = visited
        node_status = [0] * numCourses
        for i in range(numCourses):
            # node i is a new node
            if node_status[i] == 0:
                # whether there is a circle starting node i
                if self.dfs(graph, i, node_status):
                    # has a circle -> no feasible
                    return False
        # has no circle -> feasible
        return True

    def dfs(self, graph, node, node_status):
        # a visited node means no circle if dfs(node)
        if node_status[node] == 2:
            return False

        # if node is in the status of visiting, which means a circle is encountered
        if node_status[node] == 1:
            return True

        # mark node as visiting
        node_status[node] = 1
        # dfs for each neighbor
        for neighbor in graph[node]:
            if self.dfs(graph, neighbor, node_status):
                return True
        # mark node as visited, which means no circle
        node_status[node] = 2
        return False

s = TopologicalSortingSolution()
print(s.canFinish(3, [[1, 0], [2, 1]]))

