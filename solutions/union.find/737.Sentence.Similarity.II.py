class UnionFindSolution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        Given two sentences words1, words2 (each represented as an array of strings),
        and a list of similar word pairs pairs, determine if two sentences are similar.

        For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar,
        if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

        Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar,
        then "great" and "fine" are similar.

        Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

        Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

        Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

        Note:

        The length of words1 and words2 will not exceed 1000.
        The length of pairs will not exceed 2000.
        The length of each pairs[i] will be 2.
        The length of each words[i] and pairs[i][j] will be in the range [1, 20].

        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool


        """
        if not words1 and not words2:
            return True
        elif not words1 or not words2:
            return False
        elif not pairs and not self.compare(words1, words2):
            return False

        vocab = set()
        for w in words1:
            vocab.add(w)
        for w in words2:
            vocab.add(w)
        for (w1, w2) in pairs:
            vocab.add(w1)
            vocab.add(w2)

        parents = {w:w for w in vocab}
        ranks = {w:1 for w in vocab}

        for w1, w2 in pairs:
            pw1 = self.find(w1, parents)
            pw2 = self.find(w2, parents)
            if pw1 == pw2:
                continue

            if ranks[pw1] > ranks[pw2]:
                pw1, pw2 = pw2, pw1
            parents[pw1] = pw2
            ranks[pw2] += ranks[pw1]

        pwlist1 = []
        for w in words1:
            pw = self.find(w, parents)
            pwlist1.append(pw)

        pwlist2 = []
        for w in words2:
            pw = self.find(w, parents)
            pwlist2.append(pw)

        return self.compare(pwlist1, pwlist2)

    def compare(self, list1, list2):
        if len(list1) != len(list2):
            return False
        cmp = [1 if x == y else 0 for x, y in zip(sorted(list1), sorted(list2))]
        return sum(cmp) == len(list1)

    def find(self, w, parents):
        while parents[w] != w:
            parents[w] = parents[parents[w]]
            w = parents[w]
        return w

s = UnionFindSolution()
print(s.areSentencesSimilarTwo(["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]))