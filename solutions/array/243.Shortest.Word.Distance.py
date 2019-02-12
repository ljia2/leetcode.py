# class Solution: # Brute Force
#     def shortestDistance(self, words, word1, word2):
#         """
#         Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
#         Example:
#         Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
#         Input: word1 = “coding”, word2 = “practice”
#         Output: 3
#         Input: word1 = "makes", word2 = "coding"
#         Output: 1
#         Note:
#         You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
#
#         :type words: List[str]
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
#         # since the distance of two words, we can pair (i, j) and (j, i) we only need one tuple.
#         shortest = len(words)
#         for i in range(len(words)):
#             for j in range(0, i):
#                 if words[i] != words[j]:
#                     if words[i] == word1 and words[j] == word2:
#                         if shortest > abs(i-j):
#                             shortest = abs(i-j)
#                 elif words[i] == word2 and words[j] == word1:
#                     if shortest > abs(i - j):
#                         shortest = abs(i-j)
#         return shortest
#
#
# class Solution2: # Brute Force II
#     def shortestDistance(self, words, word1, word2):
#         """
#         Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
#         Example:
#         Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
#         Input: word1 = “coding”, word2 = “practice”
#         Output: 3
#         Input: word1 = "makes", word2 = "coding"
#         Output: 1
#         Note:
#         You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
#
#         :type words: List[str]
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
#         word_pos = dict()
#         for i in range(len(words)):
#             if words[i] == word1 or words[j] == word2:
#                 if words[i] in word_pos.keys():
#                     word_pos[words[i]].append(i)
#                 else:
#                     word_pos[words[i]] = [i]
#         pos_list1 = word_pos[word1]
#         pos_list2 = word_pos[word2]
#
#         shortest = len(words)
#         for i in pos_list1:
#             for j in pos_list2:
#                 if shortest > abs(i-j):
#                     shortest = abs(i-j)
#         return shortest
#
# class Solution3:
#     def shortestDistance(self, words, word1, word2):
#         """
#         Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
#         Example:
#         Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
#         Input: word1 = “coding”, word2 = “practice”
#         Output: 3
#
#         Input: word1 = "makes", word2 = "coding"
#         Output: 1
#         Note:
#         You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
#
#         :type words: List[str]
#         :type word1: str
#         :type word2: str
#         :rtype: int
#
#         since pos1 and pos2 are sorted. We use two pointers on each list
#
#         T: O(n)
#         S: O(m + p)
#         """
#         pos1 = []
#         pos2 = []
#         for i in range(len(words)):
#             if words[i] == word1:
#                pos1.append(i)
#             elif words[i] == word2:
#                 pos2.append(i)
#
#         shortest = len(words)
#         i = j = 0
#         while i < len(pos1) and j < len(pos2):
#             if shortest > abs(pos1[i]-pos2[j]):
#                 shortest = abs(pos1[i]-pos2[j])
#             if pos1[i] < pos2[j]:
#                 # when pos1[i] < pos2[j], we might get a shorter one by moving i, because moving j just make abs(i-j) bigger
#                 i += 1
#             else:
#                 # when pos1[j] < pos2[i], we might get a shorter one by moving j, because moving i just make abs(i-j) bigger
#                 j += 1
#         return shortest


class BestSolution:
    def shortestDistance(self, words, word1, word2):
        """
        Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

        Example:
        Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

        Input: word1 = “coding”, word2 = “practice”
        Output: 3
        Input: word1 = "makes", word2 = "coding"
        Output: 1
        Note:
        You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int

        since pos1 and pos2 are sorted. We use two pointers on each list

        T: O(n)
        S: O(1)

        Open Question: Fidn the shortest word distance among k words. There are two possible solutions:
        1) LC76: minimum sliding window
        2) Given K words's sorted positions, then K pointers problem (see Solution3).
           We can use priority queue to pop the least index among K words.

        """
        w1Index = -1 # recent index of word1
        w2Index = -1 # recent index of word2
        shortest = len(words)
        for i in range(len(words)):
            if words[i] != word1 and words[i] != word2:
                continue

            if words[i] == word1:
                w1Index = i
                if w1Index >= 0 and w2Index >= 0 and shortest > abs(w1Index - w2Index):
                    shortest = abs(w1Index-w2Index)
            else:
                w2Index = i
                if w1Index >= 0 and w2Index >= 0 and shortest > abs(w1Index - w2Index):
                    shortest = abs(w1Index-w2Index)
        return shortest



