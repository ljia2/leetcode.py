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

        # a neat way of initialize a dictionary key of t with value 0
        dt, ds = dict.fromkeys(t, 0), {}
        for c in t:
            dt[c] += 1

        res = ""
        max_length = 2 ** 31
        right = 0

        for i, c in enumerate(s):
            # given the left bounary i,  moving right boundary until form a valid substring
            while not self.valid(dt, ds) and right < len(s):
                ds[s[right]] = ds.get(s[right], 0) + 1
                right += 1

            if self.valid(dt, ds) and max_length > right - i:
                max_length = right - i
                res = s[i : right]
            # retreat the left boundary i of sliding window to right
            ds[c] -= 1
        return res

    def valid(self, dt, ds):
        for k in dt:
            if k not in ds or ds[k] < dt[k]:
                return False
        return True


s = BestSolution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow("a", "aa"))
print(s.minWindow("bba", "ab"))