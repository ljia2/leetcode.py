import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

        Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

        The order of output does not matter.

        Example 1:

        Input:
        s: "cbaebabacd" p: "abc"

        Output:
        [0, 6]

        Explanation:
        The substring with start index = 0 is "cba", which is an anagram of "abc".
        The substring with start index = 6 is "bac", which is an anagram of "abc".
        Example 2:

        Input:
        s: "abab" p: "ab"

        Output:
        [0, 1, 2]

        Explanation:
        The substring with start index = 0 is "ab", which is an anagram of "ab".
        The substring with start index = 1 is "ba", which is an anagram of "ab".
        The substring with start index = 2 is "ab", which is an anagram of "ab".

        :type s: str
        :type p: str
        :rtype: List[int]

        sliding window of size len(p).

        """
        if not p:
            return []
        if not s:
            return [i for i in range(len(p))]
        if len(s) < len(p):
            return []

        pcounter = collections.Counter(p)
        # set a window of size len(p).
        start = 0
        end = len(p) - 1

        scounter = collections.Counter(s[start:end + 1])
        ans = []
        while end < len(s):

            if self.isAnagrams(scounter, pcounter):
                ans.append(start)

            scounter[s[start]] -= 1
            if scounter[s[start]] == 0:
                scounter.pop[s[start]]

            start += 1
            end += 1

            # make sure end < len(s), since operate s[end] after end += 1
            if end < len(s):
                scounter[s[end]] = scounter.get(s[end], 0) + 1

        return ans

    def isAnagrams(self, scounter, pcounter):
        skeys = scounter.keys()
        pkeys = pcounter.keys()
        if len(skeys) != len(pkeys):
            return False
        for skey in skeys:
            if skey not in pkeys or scounter[skey] != pcounter[skey]:
                return False
        return True

s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
