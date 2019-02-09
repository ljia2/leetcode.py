class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

        word1 and word2 may be the same and they represent two individual words in the list.

        Example:
        Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

        Input: word1 = “makes”, word2 = “coding”
        Output: 1
        Input: word1 = "makes", word2 = "makes"
        Output: 3
        Note:
        You may assume word1 and word2 are both in the list.


        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word_pos = dict()
        for i in range(len(words)):
            if words[i] == word1 or words[i] == word2:
                if words[i] in word_pos.keys():
                    word_pos[words[i]].append(i)
                else:
                    word_pos[words[i]] = [i]

        shortest = len(words)
        if word1 == word2:
            pos_list = word_pos[word1]
            for i in range(len(pos_list)-1):
                if shortest > pos_list[i+1] - pos_list[i]:
                    shortest = pos_list[i+1] - pos_list[i]
        else:
            pos_list1 = word_pos[word1]
            pos_list2 = word_pos[word2]
            for i in pos_list1:
                for j in pos_list2:
                    if shortest > abs(i-j):
                        shortest = abs(i-j)
        return shortest