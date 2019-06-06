import collections

class Solution(object):
    def groupStrings(self, strings):
        """
        Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd".
        We can keep "shifting" which forms the sequence:

        "abc" -> "bcd" -> ... -> "xyz"
        Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

        Example:

        Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
        Output:
        [
          ["abc","bcd","xyz"],
          ["az","ba"],
          ["acef"],
          ["a","z"]
        ]
        :type strings: List[str]
        :rtype: List[List[str]]
        """

        if not strings:
            return []

        code2strings = collections.defaultdict(list)
        for s in strings:
            code = self.encode(s)
            code2strings[code].append(s)

        ans = []
        for k, v in code2strings.items():
            ans.append(v)
        return ans

    def encode(self, s):
        if len(s) == 1:
            return "-1"
        n = len(s)
        encode = []
        for i in range(n-1):
            a, b = ord(s[i]), ord(s[i+1])
            offset = str(b-a) if a <= b else str(26+b-a)
            encode.append(offset)
        return "|".join(encode)

s = Solution()
print(s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
