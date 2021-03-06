class Solution(object):
    def isAlienSorted(self, words, order):
        """
        In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
        The order of the alphabet is some permutation of lowercase letters.

        Given a sequence of words written in the alien language, and the order of the alphabet,
        return true if and only if the given words are sorted lexicographicaly in this alien language.


        Example 1:

        Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
        Output: true
        Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
        Example 2:

        Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
        Output: false
        Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
        Example 3:

        Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
        Output: false
        Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


        Note:

        1 <= words.length <= 100
        1 <= words[i].length <= 20
        order.length == 26
        All characters in words[i] and order are english lowercase letters.
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = self.build(order)
        enwords = []
        for word in words:
            enwords.append(self.translate(d, word))
        return sorted(enwords) == enwords

    def build(self, order):
        ans = dict()
        v = ord('a')
        for i, c in enumerate(order):
            ans[c] = chr(v + i)
        return ans

    def translate(self, d, word):
        return "".join(map(lambda x: d[x], word))

s = Solution()
print(s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))


class SolutionII(object):
    def isAlienSorted(self, words, order):
        """
        In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
        The order of the alphabet is some permutation of lowercase letters.

        Given a sequence of words written in the alien language, and the order of the alphabet,
        return true if and only if the given words are sorted lexicographicaly in this alien language.


        Example 1:

        Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
        Output: true
        Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
        Example 2:

        Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
        Output: false
        Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
        Example 3:

        Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
        Output: false
        Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


        Note:

        1 <= words.length <= 100
        1 <= words[i].length <= 20
        order.length == 26
        All characters in words[i] and order are english lowercase letters.
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        vocdict = self.build(order)
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            if not self.compare(w1, w2, vocdict):
                return False
        return True

    def build(self, order):
        ans = dict()
        for i, c in enumerate(order):
            ans[c] = len(ans.keys())
        return ans

    def compare(self, w1, w2, vocdict):
        l = min(len(w1), len(w2))
        for i in range(l):
            c, d = w1[i], w2[i]
            if c == d:
                continue
            if vocdict[c] > vocdict[d]:
                return False
            elif vocdict[c] < vocdict[d]:
                return True
        return len(w1) < len(w2)

s = SolutionII()
print(s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))
