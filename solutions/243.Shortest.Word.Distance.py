class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # since the distance of two words, we can pair (i, j) and (j, i) we only need one tuple.
        shortest = len(words)
        for i in range(len(words)):
            for j in range(0, i):
                if words[i] != words[j]:
                    if words[i] == word1 and words[j] == word2:
                        if shortest > abs(i-j):
                            shortest = abs(i-j)
                elif words[i] == word2 and words[j] == word1:
                    if shortest > abs(i - j):
                        shortest = abs(i-j)
        return shortest

class Solution2:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word_pos = dict()
        for i in range(len(words)):
            if words[i] == word1 or words[j] == word2:
                if words[i] in word_pos.keys():
                    word_pos[words[i]].append(i)
                else:
                    word_pos[words[i]] = [i]
        pos_list1 = word_pos[word1]
        pos_list2 = word_pos[word2]
        shortest = len(words)
        for i in pos_list1:
            for j in pos_list2:
                if shortest > abs(i-j):
                    shortest = abs(i-j)
        return shortest