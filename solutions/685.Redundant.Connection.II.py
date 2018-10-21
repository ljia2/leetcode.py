class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

        The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

        The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

        Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

        Example 1:
        Input: [[1,2], [1,3], [2,3]]
        Output: [2,3]
        Explanation: The given directed graph will be like this:
          1
         / \
        v   v
        2-->3

        Example 2:
        Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
        Output: [4,1]
        Explanation: The given directed graph will be like this:
        5 <- 1 -> 2
             ^    |
             |    v
             4 <- 3
        Note:
        The size of the input 2D-array will be between 3 and 1000.
        Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

        :type edges: List[List[int]]
        :rtype: List[int]

        case 1: If no nodes has duplicate parents, return the first edge forming a loop, (same as 684.Redundant.Connection.I)
        case 2: If a node u has two parents:
           case 2.1: If there is no loop, return the second edge (latter one)
           case 2.2: If there is loop, return {v1, u} or {v2, u} that creates the loop where v1 and v2 are two parents of u

        """

        # keep tracking the parents of each nodes
        parents = [0] * (len(edges) + 1)

        # we use roots and sizes to mimic the union find data structure.
        # keep tracking the roots of each node
        roots = [0] * (len(edges) + 1)
        # keep tracking the size of trees of node
        sizes = [1] * (len(edges) + 1)

        ans1 = []
        ans2 = []

        # first scan the edge, if there are no node with duplication parents (i.e. ans1 = ans2 = []) then remove the first edge forming the loop
        # otherwise, ans1 is the former edge (v1, u) and ans2 is the latter edge (v2, u)
        for edge in edges:
            s, d = edge
            if parents[d] > 0:
                ans1 = [parents[d], d]
                ans2 = [s, d]

                # temporally remove edge (latter one)
                edge[0] = edge[1] = -1
            parents[d] = s

        for edge in edges:
            s, d = edge
            # skip the temporally removed edge
            if s < 0 or d < 0:
                continue

            if roots[s] == 0:
                roots[s] = s
            if roots[d] == 0:
                roots[d] = d
            rs = self.find(s, roots)
            rd = self.find(d, roots)

            # ans1 = ans2 = [], then no node with duplicate parents and then remove the first edge forming loop
            # otherwise, since the latter edge is removed temporally, if a loop is formed, it must be due to ans1
            if rs == rd:
                return edge if not ans1 else ans1

            if sizes[rs] > sizes[rd]:
                rs, rd = rd, rs

            roots[rs] = rd
            sizes[rd] += sizes[rs]
        # a node with duplicate parents but either no looping is formed or the loop will be formed by ans2, return ans2
        return ans2

    def find(self, node, roots):
        while roots[node] != node:
            roots[node] = roots[roots[node]]
            node = roots[node]
        return node

s = Solution()
print(s.findRedundantDirectedConnection([[1,2],[2,3],[3,4],[4,1],[1,5]]))