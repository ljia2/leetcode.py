from collections import Counter

class Solution(object):
    def commonChars(self, A):
        """
        Given an array A of strings made only from lowercase letters,
        return a list of all characters that show up in all strings within the list (including duplicates).
        For example, if a character occurs 3 times in all strings but not 4 times,
        you need to include that character three times in the final answer.

        You may return the answer in any order.

        Example 1:

        Input: ["bella","label","roller"]
        Output: ["e","l","l"]
        Example 2:

        Input: ["cool","lock","cook"]
        Output: ["c","o"]


        Note:

        1 <= A.length <= 100
        1 <= A[i].length <= 100
        A[i][j] is a lowercase letter

        :type A: List[str]
        :rtype: List[str]
        """

        if not A:
            return []

        counters = []
        for a in A:
            counters.append(Counter(a))

        ans = []
        fcounter = counters[0]
        for k, v in fcounter.items():
            min_f = v
            found = True
            for i in range(1, len(counters)):
                if k in counters[i].keys():
                    if min_f > counters[i][k]:
                        min_f = counters[i][k]
                else:
                    found = False
                    break
            if found:
                ans += [k] * min_f
        return ans


s = Solution()
print(s.commonChars(["bella","label","roller"]))
