import collections

class WordDistance:

    def __init__(self, words):
        """
        Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters.

        Example:
        Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

        Input: word1 = “coding”, word2 = “practice”
        Output: 3
        Input: word1 = "makes", word2 = "coding"
        Output: 1
        Note:
        You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

        :type words: List[str]

        Unlimited/Multiple times implies Precompution and store with Hashtable where k = word pair and v = shortest path
        """
        self.size = len(words)
        self.word_pos = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.word_pos[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos_list1 = self.word_pos[word1]
        pos_list2 = self.word_pos[word2]
        shortest = self.size
        for i in pos_list1:
            for j in pos_list2:
                if shortest > abs(i-j):
                    shortest = abs(i-j)
        return shortest



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)