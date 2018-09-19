class Solution: # TLE
    def minWindow(self, S, T):
        """
        Given strings S and T, find the minimum (continuous) substring W of S, so that T is a subsequence of W.

        If there is no such window in S that covers all characters in T, return the empty string "".
        If there are multiple such minimum-length windows, return the one with the left-most starting index.

        Example 1:

        Input:
        S = "abcdebdde", T = "bde"
        Output: "bcde"
        Explanation:
        "bcde" is the answer because it occurs before "bdde" which has the same length.
        "deb" is not a smaller window because the elements of T in the window must occur in order.

        Note:

        All the strings in the input will only contain lowercase letters.
        The length of S will be in the range [1, 20000].
        The length of T will be in the range [1, 100].

        :type S: str
        :type T: str
        :rtype: str

        m[i][j] denote whether T[:j-1] is a subsequence of S[:i-1]

        l[i][j] = 0 if m[i][j] is False
                  minimum length of substring of S

        m[i][j] = 1) m[i-1][j-1] if S[i-1] == T[j-1]  => l[i][j] = l[i-1][j-1] + 1
                  2) m[i-1][j] if S[i-1] != T[j-1]  => l[i][j] = l[i-1][j] + 1 if m[i][j] else 0

        for m[:][len(T)] = True, find the minimum l[i][j]
        """
        if len(S) < len(T):
            return 0
        else:
            m = [[False] * (len(T) + 1) for i in range(len(S) + 1)]
            m[0][0] = True
            for i in range(1, len(S) + 1):
                m[i][0] = True

            l = [[0] * (len(T) + 1) for i in range(len(S) + 1)]

            for i in range(1, len(S) + 1):
                for j in range(1, len(T)+1):
                    if S[i-1] == T[j-1]:
                        m[i][j] = m[i-1][j-1]
                        if m[i][j]:
                            l[i][j] = l[i-1][j-1] + 1
                    else:
                        m[i][j] = m[i-1][j]
                        if m[i][j]:
                            l[i][j] = l[i-1][j] + 1
            min_length = len(S) + 1
            end = -1
            for i in range(1, len(S) + 1):
                if m[i][len(T)]:
                    if min_length > l[i][len(T)]:
                        min_length = l[i][len(T)]
                        end = i
            if end > 0 and min_length > 0:
                return S[end-min_length:end]
            else:
                return ""

class SolutionII:
    def minWindow(self, S, T):
        """
        Given strings S and T, find the minimum (continuous) substring W of S, so that T is a subsequence of W.

        If there is no such window in S that covers all characters in T, return the empty string "".
        If there are multiple such minimum-length windows, return the one with the left-most starting index.

        Example 1:

        Input:
        S = "abcdebdde", T = "bde"
        Output: "bcde"
        Explanation:
        "bcde" is the answer because it occurs before "bdde" which has the same length.
        "deb" is not a smaller window because the elements of T in the window must occur in order.

        Note:

        All the strings in the input will only contain lowercase letters.
        The length of S will be in the range [1, 20000].
        The length of T will be in the range [1, 100].

        :type S: str
        :type T: str
        :rtype: str

        m[i][j] stores the largest index k where T[:j-1] is a subsequence of S[k-1:i-1]



        m[i][j] = 1) m[i-1][j-1] if S[i-1] == T[j-1]
                  2) m[i-1][j] if S[i-1] != T[j-1]

        for m[:][len(T)] > 0, find the minimum length
        """
        if len(S) < len(T):
            return 0
        else:
            m = [[-1] * (len(T) + 1) for i in range(len(S) + 1)]
            m[0][0] = 0
            for i in range(1, len(S) + 1):
                m[i][0] = i

            for i in range(1, len(S) + 1):
                for j in range(1, len(T)+1):
                    if S[i-1] == T[j-1]:
                        m[i][j] = m[i-1][j-1]
                    else:
                        m[i][j] = m[i-1][j]

            min_length = len(S) + 1
            result = ""
            for i in range(1, len(S) + 1):
                if m[i][len(T)] > -1:
                    if min_length > i - m[i][len(T)]:
                        min_length = i - m[i][len(T)]
                        result = S[m[i][len(T)]:i]
            return result

s = SolutionII()
print(s.minWindow("abcdebdde", "bde"))
#print(s.minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u"))
#print(s.minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "k"))
#print(s.minWindow("fgrqsqsnodwmxzkzxwqegkndaa", "fnok"))





