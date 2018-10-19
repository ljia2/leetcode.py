class DFSSolution:
    def calcEquation(self, equations, values, queries):
        """
        Equations are given in the format A / B = k, where A and B are variables represented as strings,
        and k is a real number (floating point number).
        Given some queries, return the answers. If the answer does not exist, return -1.0.

        Example:
        Given a / b = 2.0, b / c = 3.0.
        queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
        return [6.0, 0.5, -1.0, 1.0, -1.0 ].

        The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries ,
        where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

        According to the example above:

        equations = [ ["a", "b"], ["b", "c"] ],
        values = [2.0, 3.0],
        queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
        The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.


        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]

        T: O(e + q*e)
        S: O(e)

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
                explored = set()
                results.append(self.dfs(graph, src, dst, explored))
        return results

    def dfs(self, graph, src, dst, explored):
        if src == dst:
            return 1.0
        # avoid cycle
        explored.add(src)
        for (node, w) in graph[src]:
            if node in explored:
                continue
            if node == dst:
                return w
            else:
                res = self.dfs(graph, node, dst, explored)
                if res >= 0.0:
                    return w * res
        return -1.0

s = DFSSolution()
print(s.calcEquation([["a","b"],["b","c"],["c", "e"],["c", "d"]], [2.0, 3.0, 1.0, 4.0], [["d", "a"], ["e", "d"]]))