class DPSolution:
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

        hint: counting ways means we need to use dynamic programming method

        dp[i] denotes the decoding ways by using the first i chars

        the question can not encode a leading 0 and two adjacent 0

        """

        if not s:
            return 0

        # have leading "0" or have two 0 in a row
        # special case.
        if s[0] == '0' or s.index("00") > -1:
            return 0

        n = len(s)
        dp = [0] * (n+1)

        # base cases: there is only 1 way to decode an empty string
        dp[0] = 1
        # base cases: there is only 1 way to decode a single digit (not zero).
        dp[1] = 1 if int(s[0]) > 0 else 0

        for i in range(2, n + 1):
            # only use the ith digit, s[i-1]
            code1 = int(s[i-1])
            # use both the i-1 and ith digits, s[i-2:i]
            code2 = int(s[i-2:i])
            # both situations are valid
            if code1 > 0 and 10 <= code2 <= 26:
                dp[i] = dp[i-1] + dp[i-2]
            # only the first situation is valid:
            elif code1 > 0:
                dp[i] = dp[i-1]
            # only the second situation is valid.
            elif 10 <= code2 <= 26:
                dp[i] = dp[i-2]
            else:
                # neither situation is valid.
                dp[i] = 0
        return dp[n]


s = DPSolution()
print(s.numDecodings("226"))
print(s.numDecodings("236"))
print(s.numDecodings("0"))
print(s.numDecodings("12"))
print(s.numDecodings("00"))
