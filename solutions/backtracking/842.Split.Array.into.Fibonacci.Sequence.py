class Solution:
    def splitIntoFibonacci(self, S):
        """
        Given a string S of digits, such as S = "123456579",
        we can split it into a Fibonacci-like sequence [123, 456, 579].

        Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

        0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
        F.length >= 3; and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
        Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes,
        except if the piece is the number 0 itself.

        Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

        Example 1:

        Input: "123456579"
        Output: [123,456,579]
        Example 2:

        Input: "11235813"
        Output: [1,1,2,3,5,8,13]
        Example 3:

        Input: "112358130"
        Output: []
        Explanation: The task is impossible.
        Example 4:

        Input: "0123"
        Output: []
        Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
        Example 5:

        Input: "1101111"
        Output: [110, 1, 111]
        Explanation: The output [11, 0, 11, 11] would also be accepted.
        Note:

        1 <= S.length <= 200
        S contains only digits.

        :type S: str
        :rtype: List[int]

        1 <= S.length <= 200 hints O(n^3)

        given s[:i], s[i:j], backtracking/dfs on s[j:] to generate fibnonacci sequence

        """

        if not S or len(S) <= 2:
            return []

        ans = []
        self.dfs(S, [], ans)
        return ans

        ans = []
        prenums = []
        for i in range(1, len(S)-2):
            for j in range(i+1, len(S)-1):
                num1 = int(S[:i])
                num2 = int(S[i:j])
                if num1 > 2**31 - 1 or num2 > 2**31 - 1:
                    continue

                prenums.append(num1)
                prenums.append(num2)
                self.dfs(num1, num2, S[j:], prenums, ans)
                # branch pruning. if one branch has found fib seq, return true to upper call
                if ans:
                    return ans
                prenums.pop()
                prenums.pop()
        return ans

    def dfs(self, num1, num2, S, prenums, ans):
        if not S:
            ans.extend(prenums)
            return

        num3 = num1 + num2
        if num3 > 2**31 - 1:
            return
        # S does not contain num3 at the beginning
        if S.find(str(num3)) != 0:
            return
        # add num3 to prenums
        prenums.append(num3)
        # keep bfs on S[len(str(num3)):]
        self.dfs(num2, num3, S[len(str(num3)):], prenums, ans)
        # pop num3 for backtracking.
        prenums.pop()
        return

s = Solution()
print(s.splitIntoFibonacci("11235813"))