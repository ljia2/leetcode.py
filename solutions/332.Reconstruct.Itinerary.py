from heapq import heappush, heappop
class Solution:
    def findItinerary(self, tickets):
        """

        Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
        reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK.
        Thus, the itinerary must begin with JFK.

        Note:

        If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
        For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
        All airports are represented by three capital letters (IATA code).
        You may assume all tickets form at least one valid itinerary.
        Example 1:

        Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

        Example 2:

        Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
        Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
                     But it is larger in lexical order.

        :type tickets: List[List[str]]
        :rtype: List[str]

        DFS + Backtracking on Graph

        Time: O(n + nlogn + n!) where O(n + nlogn) is building graph and n! is the backtracking on the graph.
        Space: O(n) store the graph


        """
        if not tickets:
            return []
        # sorting the destinations by lexical ordering
        tickets.sort(key=lambda x:x[1])
        graph = self.build_graph(tickets)
        return self.dfs(graph, "JFK", len(tickets)+1)[0]

    def build_graph(self, tickets):
        g = dict()
        for t in tickets:
            s, d = t
            if s in g.keys():
                g[s].append(d)
            else:
                g[s] = [d]
        return g

    def dfs(self, graph, start, total_length):
        if start in graph.keys():
            num_dest = len(graph[start])
            for i in range(num_dest):
                # remove the edge from start to destinations[i] to avoid loop
                d = graph[start].pop(i)
                results = self.dfs(graph, d, total_length-1)
                for res in results:
                    if len(res) == total_length - 1:
                        return [[start] + res]
                # Note that add the edge back for dfs for destinations[i+1] for backtrack !!!!!!
                graph[start].insert(i, d)
        return [[start]]


class BestSolution:
    def findItinerary(self, tickets):
        """

        Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
        reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK.
        Thus, the itinerary must begin with JFK.

        Note:

        If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
        For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
        All airports are represented by three capital letters (IATA code).
        You may assume all tickets form at least one valid itinerary.
        Example 1:

        Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
        Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

        Example 2:

        Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
        Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
                     But it is larger in lexical order.

        :type tickets: List[List[str]]
        :rtype: List[str]


        In graph theory, an Eulerian trail (or Eulerian path) is a trail in a finite graph which visits every edge exactly once. (use all ticekts once)
        1) graph is connected
        2) staisfying either conditions
           a) only one node whose in-degree is less than out degree (as start); only one node whose in-degree is one more than out-degree (as end point); all other nodes whose in-degrees are equal to out-degrees
           b) all nodes whose in-degree is equal to its out-degree

        Then the graph must have a Eulerian trail.

        Similarly, an Eulerian circuit or Eulerian cycle is an Eulerian trail which starts and ends on the same vertex.

        Based on the description of 332, it is a directly application Hierholzer's algorithm on the graph


        Employ Hierholzer’s Algorithm

        T: O(n + nlogn + n)
        S: O(n)

        """

        if not tickets:
            return []

        graph = dict()
        for t in tickets:
            s, d = t
            if s not in graph.keys():
                graph[s] = []
            heappush(graph[s], d)

        results = []
        self.dfs("JFK", results, graph)

        return results

    def dfs(self, start, results, graph):
        while graph[start]:
            self.dfs(heappop(graph[start]), results, graph)
        results.insert(0, start)


s = BestSolution()
print(s.findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]))