class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        There are 8 prison cells in a row, and each cell is either occupied or vacant.

        Each day, whether the cell is occupied or vacant changes according to the following rules:

        If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied. Otherwise, it becomes vacant.

        (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

        We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

        Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)



        Example 1:

        Input: cells = [0,1,0,1,1,0,0,1], N = 7
        Output: [0,0,1,1,0,0,0,0]
        Explanation:
        The following table summarizes the state of the prison on each day:
        Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
        Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
        Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
        Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
        Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
        Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
        Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
        Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

        Example 2:

        Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
        Output: [0,0,1,1,1,1,1,0]


        Note:

        cells.length == 8
        cells[i] is in {0, 1}
        1 <= N <= 10^9

        :type cells: List[int]
        :type N: int
        :rtype: List[int]

        It will get TLE when N is big.
        Note that cells.length = 8, and cells[0] and cells[7] will become 0.
        In fact, cells have only 2 ^ 6 = 64 different states.
        And there will be a loop.

        1 <= N <= 10^9 hints some trick to avoid linear.
        """
        visited = dict()
        while N:
            visited[str(cells)] = N
            N -= 1

            ncells = [0] * len(cells)
            for i, v in enumerate(cells):
                if i == 0 or i == len(cells)-1:
                    ncells[i] = 0
                elif cells[i-1] == cells[i+1]:
                    ncells[i] = 1
                else:
                    ncells[i] = 0
            cells = ncells

            # state repeats after (visited[str(cells)] - N) loops
            if str(cells) in visited.keys():
                N %= visited[str(cells)] - N
        return cells

s = Solution()
print(s.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000))