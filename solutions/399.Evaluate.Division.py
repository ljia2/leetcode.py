class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = dict()
        for index in range(len(equations)):
            a, b = equations[index][0], equations[index][1]
            w = values[index]

            if a not in graph.keys():
                graph[a] = [(b, w)]
            else:
                graph[a].append((b, w))

            if b not in graph.keys():
                graph[b] = [(a, 1.0/w)]
            else:
                graph[b].append((a, 1.0/w))

        results = []
        for q in queries:
            src, dst = q
            if src not in graph.keys() or dst not in graph.keys():
                results.append(-1.0)
            elif src == dst:
                results.append(1.0)
            else:
                explored = [src]
                results.append(self.searchGraph(graph, src, dst, explored))
        return results

    def searchGraph(self, graph, src, dst, explored):
        # check the direct edge
        stack = []
        for (node, w) in graph[src]:
            if node in explored:
                continue
            if node == dst:
                return w
            else:
                stack.append((node, w))
        # DFS search
        while stack:
            new_src, w = stack.pop()
            explored.append(new_src)
            print(explored)
            res = self.searchGraph(graph, new_src, dst, explored)
            if res >= 0.0:
                return w * res
        return -1.0


s = Solution()
print(s.calcEquation([["a","b"],["b","c"],["c", "e"],["c", "d"]], [2.0, 3.0, 1.0, 4.0], [["d", "a"], ["e", "d"]]))