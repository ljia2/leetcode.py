from collections import Counter

class BestSolution:
    def minWindow(self, s, t):
        """
        Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

        Example:

        Input: S = "ADOBECODEBANC", T = "ABC"
        Output: "BANC"
        Note:

        If there is no such window in S that covers all characters in T, return the empty string "".
        If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

        :type s: str
        :type t: str
        :rtype: str

        classic sliding window idea!!!

        """
        if not s or not t or len(s) < len(t) or len(s) * len(t) == 0:
            return ""

        dt = Counter(t)
        ns = []
        for i, c in enumerate(s):
            if c in dt.keys():
                ns.append((i, c))

        # a neat way of initialize a dictionary key of t with value 0
        swindow = dict()
        # use a tuple to store the answer
        ans = float("inf"), None, None

        l = r = 0

        uct = len(dt)
        ucs = 0

        for r in range(len(ns)):
            end_index, c = ns[r]
            # expanding the ds of the sliding window
            swindow[c] = swindow.get(c, 0) + 1

            # if a char in the sliding window first meet the frequency in t.
            if swindow[c] == dt[c]:
                ucs += 1

            # when a valid window is formed, start retreating the left of the window
            while l <= r and ucs == uct:
                start_index, d = ns[l]

                if end_index - start_index + 1 < ans[0]:
                    ans = end_index - start_index + 1, start_index, end_index

                # retreat the left of window
                # if the window is no longer valid (ucs != uct), stop retreating the left
                swindow[d] -= 1
                if swindow[d] < dt[d]:
                    ucs -= 1
                l += 1
            r += 1

        # unpack the answer
        return None if ans[1] == float("inf") else s[ans[1]:ans[2]+1]


s = BestSolution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("a", "aa"))
print(s.minWindow("bba", "ab"))