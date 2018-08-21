class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.size = len(words)
        self.word_pos = dict()
        for i in range(len(words)):
            word = words[i]
            if word in self.word_pos.keys():
                self.word_pos[word].append(i)
            else:
                self.word_pos[word] = [i]

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