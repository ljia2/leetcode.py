class Solution:
    def numDecodings(self, s):
        """

        A message containing letters from A-Z is being encoded to numbers using the following mapping:

        'A' -> 1
        'B' -> 2
        ...
        'Z' -> 26
        Given a non-empty string containing only digits, determine the total number of ways to decode it.

        Example 1:

        Input: "12"
        Output: 2
        Explanation: It could be decoded as "AB" (1 2) or "L" (12).
        Example 2:

        Input: "226"
        Output: 3
        Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

        :type s: str
        :rtype: int

        dp[j] = dp[i][j-2] * (1 if s[j-2:j] is a valid code else 0) + dp[j-1] * (1 if s[j-1:j] is a valid code else 0)

        """

        if not s:
            return 0
        else:
            sl = len(s) + 1
            dp = [0] * sl
            # base case initialization
            for j in range(1, sl, 1):
                if j == 1:
                    code1 = int(s[j-1:j])
                    if code1 > 0:
                        dp[j] = 1
                    else:
                        dp[j] = 0
                elif j == 2:
                    code1 = int(s[j-1:j])
                    code2 = int(s[j-2:j])
                    if 10 <= code2 <= 26 and code1 > 0:
                        dp[j] = 1 + dp[j-1]
                    elif code1 > 0:
                        dp[j] = dp[j-1]
                    elif 10 <= code2 <= 26:
                        dp[j] = 1
                    else:
                        dp[j] = 0
                else:
                    code1 = int(s[j-1:j])
                    code2 = int(s[j-2:j])
                    if 10 <= code2 <= 26 and code1 > 0:
                        dp[j] = dp[j-2] + dp[j-1]
                    elif code1 > 0:
                        dp[j] = dp[j-1]
                    elif 10 <= code2 <= 26:
                        dp[j] = dp[j-2]
                    else:
                        dp[j] = 0
            return dp[len(s)]

s = Solution()
print(s.numDecodings("226"))
print(s.numDecodings("236"))
print(s.numDecodings("0"))
print(s.numDecodings("102"))

