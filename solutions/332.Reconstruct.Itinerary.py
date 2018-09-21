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
        """
        if not tickets:
            return []
        tickets.sort(key=lambda x:x[1])
        graph = self.buildGraph(tickets)
        return self.dfs(graph, "JFK", len(tickets)+1)[0]

    def buildGraph(self, tickets):
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
                # add the edge back for dfs for destinations[i+1]
                graph[start].insert(i, d)
        return [[start]]

s = Solution()
print(s.findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]))