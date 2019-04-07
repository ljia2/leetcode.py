class Solution(object): # TLE
    def baseNeg2(self, N):
        """
        Given a number N, return a string consisting of "0"s and "1"s that represents its value in base -2 (negative two).

        The returned string must have no leading zeroes, unless the string is "0".

        Example 1:

        Input: 2
        Output: "110"
        Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
        Example 2:

        Input: 3
        Output: "111"
        Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
        Example 3:

        Input: 4
        Output: "100"
        Explantion: (-2) ^ 2 = 4

        Note:

        0 <= N <= 10^9
        :type N: int
        :rtype: str


        use dfs on string 0 if N % 2 == 0
                          1 if N % 2 == 1
        """
        return self.bfs(N)

    def bfs(self, N):
        if N % 2 == 0:
            q = [("0", 0)]
        else:
            q = [("1", 1)]

        while q:
            size = len(q)
            while size > 0:
                # POP AS a QUEUE!!!!
                numstr, num = q.pop(0)
                size -= 1

                if num == N:
                    return numstr

                for d in [0, 1]:
                    level = len(numstr)

                    new_num = ((-2)**level + num) if d == 1 else num
                    new_numstr = str(d) + numstr

                    if new_num > N:
                        continue
                    q.append((new_numstr, new_num))
        return None


s = Solution()
print(s.baseNeg2(6))
print(s.baseNeg2(8))
print(s.baseNeg2(63628))
