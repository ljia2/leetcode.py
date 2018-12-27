from collections import defaultdict
# class Solution: # TLE
#     def numBusesToDestination(self, routes, S, T):
#         """
#         We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever.
#         For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence
#         1->5->7->1->5->7->1->... forever.
#         We start at bus stop S (initially not on a bus), and we want to go to bus stop T.
#         Travelling by buses only, what is the least number of buses we must take to reach our destination?
#         Return -1 if it is not possible.
#
#         Example:
#         Input:
#         routes = [[1, 2, 7], [3, 6, 7]]
#         S = 1
#         T = 6
#         Output: 2
#         Explanation:
#         The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
#
#         Note:
#         1 <= routes.length <= 500.
#         1 <= routes[i].length <= 500.
#         0 <= routes[i][j] < 10 ^ 6.
#
#         :type routes: List[List[int]]
#         :type S: int
#         :type T: int
#         :rtype: int
#         """
#         if S == T:
#             return 0
#         graph = defaultdict(list)
#         for i in range(len(routes)):
#             route = routes[i]
#             for j in range(len(route)):
#                 for k in range(j+1, len(route)):
#                     graph[route[j]].append((route[k], i))
#                     graph[route[k]].append((route[j], j))
#
#         qe = [(S, set())]
#         visited = set()
#         visited.add(S)
#
#         while qe:
#             size = len(qe)
#             while size > 0:
#                 stop, buses = qe.pop(0)
#                 size -= 1
#
#                 if stop == T:
#                     return len(buses)
#
#                 for nstop, bus in graph[stop]:
#                     if nstop in visited or bus in buses:
#                         continue
#                     # Note that we need a deep copy to aviod reference change
#                     nbuses = buses.copy()
#                     nbuses.add(bus)
#
#                     qe.append((nstop, nbuses))
#                     visited.add(nstop)
#         return -1

class SolutionII:
    def numBusesToDestination(self, routes, S, T):
        """
        We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever.
        For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence
        1->5->7->1->5->7->1->... forever.
        We start at bus stop S (initially not on a bus), and we want to go to bus stop T.
        Travelling by buses only, what is the least number of buses we must take to reach our destination?
        Return -1 if it is not possible.

        Example:
        Input:
        routes = [[1, 2, 7], [3, 6, 7]]
        S = 1
        T = 6
        Output: 2
        Explanation:
        The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

        Note:
        1 <= routes.length <= 500.
        1 <= routes[i].length <= 500.
        0 <= routes[i][j] < 10 ^ 6.

        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int

        Note that, this quesiton asks how many buses.

        This solutions is use buses as the node. stops for each bus (node) for auxiliary information.
        bus nodes are connected if they share a stop.

        BFS on the bus graph. Whenever expand on the graph. we need collect all stops to determine whether reaching T.

        """
        if S == T:
            return 0
        # build the graph of stop -> [buses]
        stop2buses = defaultdict(list)
        for i in range(len(routes)):
            route = routes[i]
            for stop in route:
                stop2buses[stop].append(i)

        used_buses = [0] * len(routes)
        qe = [S]
        buses = 0
        while qe:
            size = len(qe)
            while size > 0:
                stop = qe.pop(0)
                size -= 0

                if stop == T:
                    return buses

                for bus in stop2buses[stop]:
                    if used_buses[bus] == 1:
                        continue
                    used_buses[bus] = 1
                    for stop in routes[bus]:
                        qe.append(stop)

            buses += 1
        return -1



s = SolutionII()
print(s.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))