import collections

class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        On a N x N grid of cells, each cell (x, y) with 0 <= x < N and 0 <= y < N has a lamp.

        Initially, some number of lamps are on.  lamps[i] tells us the location of the i-th lamp that is on.
        Each lamp that is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to a Queen in chess).

        For the i-th query queries[i] = (x, y), the answer to the query is 1 if the cell (x, y) is illuminated, else 0.

        After each query (x, y) [in the order given by queries], we turn off any lamps that are at cell (x, y)
        or are adjacent 8-directionally (ie., share a corner or edge with cell (x, y).)

        Return an array of answers.  Each value answer[i] should be equal to the answer of the i-th query queries[i].



        Example 1:

        Input: N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
        Output: [1,0]
        Explanation:
        Before performing the first query we have both lamps [0,0] and [4,4] on.
        The grid representing which cells are lit looks like this, where [0,0] is the top left corner, and [4,4] is the bottom right corner:
        1 1 1 1 1
        1 1 0 0 1
        1 0 1 0 1
        1 0 0 1 1
        1 1 1 1 1
        Then the query at [1, 1] returns 1 because the cell is lit.  After this query, the lamp at [0, 0] turns off, and the grid now looks like this:
        1 0 0 0 1
        0 1 0 0 1
        0 0 1 0 1
        0 0 0 1 1
        1 1 1 1 1
        Before performing the second query we have only the lamp [4,4] on.  Now the query at [1,0] returns 0, because the cell is no longer lit.


        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]

        Note:

        1 <= N <= 10^9
        0 <= lamps.length <= 20000
        0 <= queries.length <= 20000
        lamps[i].length == queries[i].length == 2

        given a lamp at (i, j), it covers (h, i), (v, j), ('d', i+j), ('rd', N - j + i - 1).
        1) build dictionary to lamps to lines.
        2) build dictionary to lines to lambs.

        for each query,
           1) check its illumuation.
           2) remove lamps at 8-directional adjacent;
           3) update lamps and line dictionary

        """

        if not lamps:
            return [0] * len(queries)

        if not queries:
            return []

        hldict = collections.defaultdict(set)
        vldict = collections.defaultdict(set)
        fddict = collections.defaultdict(set)
        rddict = collections.defaultdict(set)

        for lamp in lamps:
            x, y = lamp
            hldict[y].add((x, y))
            vldict[x].add((x, y))
            fddict[x+y].add((x, y))
            rddict[N-y+x-1].add((x, y))

        lampset = set(map(lambda x: (x[0], x[1]), lamps))

        ans = []
        for query in queries:
            x, y = query
            if hldict[y] or vldict[x] or fddict[x+y] or rddict[N-y+x-1]:
                ans.append(1)
            else:
                ans.append(0)

            for nx, ny in [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]:
                if nx < 0 or ny < 0 or nx >= N or ny >= N or (nx, ny) not in lampset:
                    continue

                hldict[ny].remove((nx, ny))
                vldict[nx].remove((nx, ny))
                fddict[nx+ny].remove((nx, ny))
                rddict[N-ny+nx-1].remove((nx, ny))
                lampset.remove((nx, ny))

        return ans

s = Solution()
print(s.gridIllumination(5, [[0,0],[4,4]], [[1,1],[1,0]]))
