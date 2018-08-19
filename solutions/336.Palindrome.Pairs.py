class Solution(object):

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        if words is None or len(words) == 0:
            return []
        results = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if self.isPalindrom(words[i], words[j]):
                        results.append([i, j])
        return results

    def isPalindrom(self, w1, w2):
        w = w1 + w2
        s = 0
        e = len(w)-1
        while s <= e:
            if w[s] == w[e]:
                s += 1
                e -= 1
            else:
                return False
        return True

