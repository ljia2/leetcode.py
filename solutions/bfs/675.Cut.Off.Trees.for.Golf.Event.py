from heapq import heappush, heappop
import copy

class Solution(object):
    def cutOffTree(self, forest):
        """
        You are asked to cut off trees in a forest for a golf event.
        The forest is represented as a non-negative 2D map, in this map:

        0 represents the obstacle can't be reached.
        1 represents the ground can be walked through.
        The place with number bigger than 1 represents a tree can be walked through,
        and this positive number represents the tree's height.

        You are asked to cut off all the trees in this forest in the order of tree's height -
        always cut off the tree with lowest height first.
        And after cutting, the original place has the tree will become a grass (value 1).

        You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees.
        If you can't cut off all the trees, output -1 in that situation.

        You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

        Example 1:

        Input:
        [
         [1,2,3],
         [0,0,4],
         [7,6,5]
        ]
        Output: 6


        Example 2:

        Input:
        [
         [1,2,3],
         [0,0,0],
         [7,6,5]
        ]
        Output: -1


        Example 3:

        Input:
        [
         [2,3,4],
         [0,0,5],
         [8,7,6]
        ]
        Output: 6
        Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.


        Hint: size of the given matrix will not exceed 50x50.

        :type forest: List[List[int]]
        :rtype: int

        for each target:
            initialize queue with all glass positions.
            do dfs to reach target by step
            ans += step
        """

        if not forest or not forest[0]:
            return 0

        hq = []
        for r in range(len(forest)):
            for c in range(len(forest[0])):
                if forest[r][c] > 1:
                    heappush(hq, (forest[r][c], r, c))
        ans = 0
        startr = startc = 0
        while hq:
            tree, r, c = heappop(hq)
            step = self.minStep(forest, startr, startc, tree)
            if step < 0:
                return -1
            else:
                ans += step
                startr, startc = r, c
        return ans

    def minStep(self, forest, startr, startc, tree):
        # start from the last cutting location.
        q = [(startr, startc)]
        visited = [[False for _ in range(len(forest[0]))] for _ in range(len(forest))]
        visited[startr][startc] = True

        step = 0
        while q:
            size = len(q)
            while size > 0:
                r, c = q.pop(0)
                size -= 1

                if forest[r][c] == tree:
                    # cut the tree
                    forest[r][c] = 1
                    return step

                for nr, nc in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
                    if nr < 0 or nc < 0 or nr >= len(forest) or nc >= len(forest[0]):
                        continue
                    if forest[nr][nc] == 0 or visited[nr][nc]:
                        continue
                    visited[nr][nc] = True
                    q.append((nr, nc))
            step += 1
        return -1

s = Solution()
# print(s.cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))
# print(s.cutOffTree([[2,3,4],[0,0,5],[8,7,6]]))
# print(s.cutOffTree([[1,2,3],[0,0,0],[7,6,5]]))
print(s.cutOffTree([[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]]))