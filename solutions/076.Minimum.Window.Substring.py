class Solution(object): # TLE
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

        Note that O(n) hints two pointers
        """

        if not t:
            return ""

        tdict = dict()
        for c in t:
            if c not in tdict.keys():
                tdict[c] = 1
            else:
                tdict[c] += 1

        min_window = ""
        start = 0
        while start < len(s):
            if s[start] not in tdict.keys():
                start += 1
            else:
                end = start
                sdict = dict()
                while end < len(s):
                    if s[end] in tdict.keys():
                        if s[end] not in sdict.keys():
                            sdict[s[end]] = 1
                        else:
                            sdict[s[end]] += 1
                        if self.isValidMap(tdict, sdict):
                            break
                        else:
                            end += 1
                    else:
                        end += 1

                if end == len(s):
                    break
                else:
                    # skip the unnecessary prefix from target in order to get the minimum window
                    while s[start] not in sdict.keys() or sdict[s[start]] > tdict[s[start]]:
                        if s[start] in sdict.keys() and sdict[s[start]] > tdict[s[start]]:
                            sdict[s[start]] -= 1
                        start += 1

                    if min_window == "" or len(min_window) > end - start + 1:
                        min_window = s[start:end+1]

                    # keep moving start until sdict size just less than tdict
                    while start < len(s) and self.isValidMap(tdict, sdict):
                        if s[start] in sdict.keys():
                            if sdict[s[start]] == 1:
                                sdict.pop(s[start])
                            else:
                                sdict[s[start]] -= 1
                        start += 1

        return min_window

    def isValidMap(self, t, s):
        if len(t) == len(s):
            for (k, v) in t.items():
                if k in s.keys() and s[k] >= v:
                    continue
                else:
                    return False
            return True
        else:
            return False


class BestSolution:
    def minWindow(self, s , t):
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

        Note that O(n) hints two pointers
        """
        if not s or not t or len(s) < len(t) or len(s) * len(t) == 0:
            return ""
        dt, ds = dict.fromkeys(t, 0), {}
        for c in t:
            dt[c] += 1

        res = ""
        max_length = 2 ** 31
        right = 0
        for i, c in enumerate(s):
            # moving right until form a valid substring
            while (not self.valid(dt, ds)) and right < len(s):
                ds[s[right]] = ds.get(s[right], 0) + 1
                right += 1

            if self.valid(dt, ds) and max_length > right - i:
                max_length = right - i
                res = s[i : right]
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