class Solution(object):
    def customSortString(self, S, T):
        """
        S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

        S was sorted in some custom order previously. We want to permute the characters of T
        so that they match the order that S was sorted.
        More specifically, if x occurs before y in S, then x should occur before y in the returned string.

        Return any permutation of T (as a string) that satisfies this property.

        Example :
        Input:
        S = "cba"
        T = "abcd"
        Output: "cbad"
        Explanation:
        "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
        Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.


        Note:

        S has length at most 26, and no character is repeated in S.
        T has length at most 200.
        S and T consist of lowercase letters only.

        :type S: str
        :type T: str
        :rtype: str
        """
        if not S:
            raise Exception("Invalid Input!")

        if not T:
            return T

        encode_dict = dict()
        decode_dict = dict()
        size = 0
        for s in S:
            encode_dict[s] = size
            decode_dict[size] = s
            size += 1

        codet = self.encode(encode_dict, T)
        codet.sort()
        return self.decode(decode_dict, codet)

    def encode(self, edict, T):
        ans = []
        for t in T:
            ans.append(edict.get(t, ord(t)))
        return ans

    def decode(self, ddict, T_code):
        ans = ""
        for tc in T_code:
            ans += ddict.get(tc, chr(tc))
        return ans

class SolutionII(object):
    def customSortString(self, S, T):
        """
        S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

        S was sorted in some custom order previously. We want to permute the characters of T
        so that they match the order that S was sorted.
        More specifically, if x occurs before y in S, then x should occur before y in the returned string.

        Return any permutation of T (as a string) that satisfies this property.

        Example :
        Input:
        S = "cba"
        T = "abcd"
        Output: "cbad"
        Explanation:
        "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
        Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.


        Note:

        S has length at most 26, and no character is repeated in S.
        T has length at most 200.
        S and T consist of lowercase letters only.

        :type S: str
        :type T: str
        :rtype: str
        """
        if not S:
            raise Exception("Invalid Input!")

        if not T:
            return T

        encode_dict = dict()
        for s in S:
            encode_dict[s] = chr(len(encode_dict) + ord('a'))
        return "".join(sorted(list(T), key=lambda x: self.encode(x, encode_dict)))

    def encode(self, word, edict):
        ans = ""
        for c in word:
            ans += edict.get(c, c)
        return ans


s = SolutionII()
print(s.customSortString("cba", "abcd"))