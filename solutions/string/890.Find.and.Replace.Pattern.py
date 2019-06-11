class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        You have a list of words and a pattern, and you want to know which words in words matches the pattern.

        A word matches the pattern if there exists a permutation of letters p
        so that after replacing every letter x in the pattern with p(x), we get the desired word.

        (Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter,
        and no two letters map to the same letter.)

        Return a list of the words in words that match the given pattern.

        You may return the answer in any order.

        Example 1:

        Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
        Output: ["mee","aqq"]
        Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
        "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
        since a and b map to the same letter.


        Note:

        1 <= words.length <= 50
        1 <= pattern.length = words[i].length <= 20


        :type words: List[str]
        :type pattern: str
        :rtype: List[str]

        bijection is one to one
        similar to LC205
        """
        if not words:
            return words

        if not pattern:
            return []

        ans = []
        for word in words:
            if self.isIsomorphic(word, pattern):
                ans.append(word)
        return ans

    def isIsomorphic(self, word, pattern):
        if len(word) != len(pattern):
            return False

        a2b = dict()
        for i in range(len(word)):
            a, b = word[i], pattern[i]
            if a not in a2b.keys():
                if b not in a2b.values():
                    a2b[a] = b
                else:
                    return False
            else:
                if a2b[a] == b:
                    continue
                else:
                    return False
        return True




