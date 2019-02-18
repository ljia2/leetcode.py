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
        ways[i] denotes the decoding ways by using the first i chars

        """

        if not s:
            return 0

        ways = [0] * (len(s) + 1)
        # base cases: there is only 1 way to decode empty string
        ways[0] = 1
        for i in range(1, len(s) + 1):
            if i == 1:
                code1 = int(s[i-1])
                if code1 > 0:
                    ways[i] = 1
                else:
                    ways[i] = 0
            else:
                code2 = int(s[i-2:i])
                code1 = int(s[i-1])
                if code1 > 0 and 10 <= code2 <= 26:
                    ways[i] = ways[i-1] + ways[i-2]
                elif code1 > 0:
                    ways[i] = ways[i-1]
                elif 10 <= code2 <= 26:
                    ways[i] = ways[i-2]
                else:
                    ways[i] = 0
        return ways[-1]


s = DPSolution()
print(s.numDecodings("226"))
print(s.numDecodings("236"))
print(s.numDecodings("0"))
print(s.numDecodings("12"))

