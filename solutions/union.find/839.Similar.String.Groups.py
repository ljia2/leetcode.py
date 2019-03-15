class UnionFindSolution:
    def numSimilarGroups(self, A): # TLE
        """
        Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.

        For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

        Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.
        Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

        We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

        Example 1:

        Input: ["tars","rats","arts","star"]
        Output: 2
        Note:

        A.length <= 2000
        A[i].length <= 1000
        A.length * A[i].length <= 20000
        All words in A consist of lowercase letters only.
        All words in A have the same length and are anagrams of each other.
        The judging time limit has been increased for this question.

        :type A: List[str]
        :rtype: int

        When two words are similar, they are considered connected.
        Employ Union Find Algorithm to fidn the number of connected components.
        
        """
        if not A:
            return 0
        if len(A) == 1:
            return 1

        # use dictionary to represent parents and ranks.
        parents = {w:w for w in A}
        ranks = {w:1 for w in A}

        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if self.similar(A[i], A[j]):
                    self.union(A[i], A[j], parents, ranks)

        groups = set()
        for w in A:
            pw = self.find(w, parents)
            groups.add(pw)
        return len(groups)

    def find(self, w, parents):
        while w != parents[w]:
            parents[w] = parents[parents[w]]
            w = parents[w]
        return w

    def union(self, w1, w2, parents, ranks):
        p1 = self.find(w1, parents)
        p2 = self.find(w2, parents)
        if p1 == p2:
            return
        if ranks[p1] > ranks[p2]:
            p1, p2 = p2, p1
        parents[p1] = p2
        ranks[p2] += ranks[p1]
        return

    def similar(self, w1, w2):
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
            if diff > 2:
                return False
        return True

s = UnionFindSolution()
print(s.numSimilarGroups(["tars","rats","arts","star"]))