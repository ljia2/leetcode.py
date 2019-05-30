from collections import defaultdict


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
        The input is always valid. You may assume that evaluating the queries will result in no division by zero
        and there is no contradiction.


        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]

        T: O(e + q*e)
        S: O(e)

        """

        graph = defaultdict(list)
        for index in range(len(equations)):
            a, b = equations[index][0], equations[index][1]
            w = values[index]
            graph[a].append[(b, w)]
            graph[b].append((a, 1.0/w))

        ans = []
        for q in queries:
            src, dst = q
            if src not in graph.keys() or dst not in graph.keys():
                ans.append(-1.0)
            elif src == dst:
                ans.append(1.0)
            else:
                ans.append(self.dfs(graph, src, dst, set()))
        return ans

    def dfs(self, graph, src, dst, visited):
        if src == dst:
            return 1.0

        # avoid cycle
        visited.add(src)
        for (node, w) in graph[src]:
            if node in visited:
                continue

            if node == dst:
                return w
            else:
                res = self.dfs(graph, node, dst, visited)
                # if res is -1.0, there is no path to dst.
                if res >= 0.0:
                    return w * res
        return -1.0

s = DFSSolution()
print(s.calcEquation([["a","b"],["b","c"],["c", "e"],["c", "d"]], [2.0, 3.0, 1.0, 4.0], [["d", "a"], ["e", "d"]]))

#### Union Find Solution
class UnionFindSolution:
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

        """
        def find(x):
            while x != parents[x][0]:
                px, pv = parents(parents[x][0])
                parents[x] = (px, parents[x][1] * pv)
            return parents[x]

        def divide(x, y):
            rx, vx = find(x)
            ry, vy = find(y)
            if rx != ry:
                return -1.0
            return vx / vy

        parents = dict()
        for (x, y), v in zip(equations, values):
            if x not in parents and y not in parents:
                # x = y * v
                parents[x] = (y, v)
                parents[y] = (y, 1.0)
            elif x not in parents:
                # x = y * v
                parents[x] = (y, v)
            elif y not in parents:
                # y = x * 1 / v
                parents[y] = (x, 1.0 / v)
            else:
                # x = rx * vx
                rx, vx = find(x)
                # y = ry * vy
                ry, vy = find(y)
                # x = y * v -> rx = x / vx = y * v / vx => rv * (vy * v / vx)
                parents[rx] = (ry, v / vx * vy)

        ans = [divide(x, y) if x in parents and y in parents else -1 for x, y in queries]
        return ans
