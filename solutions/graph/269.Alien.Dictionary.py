from collections import defaultdict

class Solution(object):
    def alienOrder(self, words):
        """
        There is a new alien language which uses the latin alphabet.
        However, the order among letters are unknown to you.
        You receive a list of non-empty words from the dictionary,
        where words are sorted lexicographically by the rules of this new language.
        Derive the order of letters in this language.

        Example 1:

        Input:
        [
          "wrt",
          "wrf",
          "er",
          "ett",
          "rftt"
        ]

        Output: "wertf"
        Example 2:

        Input:
        [
          "z",
          "x"
        ]

        Output: "zx"
        Example 3:

        Input:
        [
          "z",
          "x",
          "z"
        ]

        Output: ""

        Explanation: The order is invalid, so return "".
        Note:

        You may assume all letters are in lowercase.
        You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
        If the order is invalid, return an empty string.
        There may be multiple valid order of letters, return any one of them is fine.
        
        :type words: List[str]
        :rtype: str
        """

        if not words:
            return ""

        if len(words) == 1:
            return words[0][::-1]

        indict = defaultdict(set)
        outdict = defaultdict(set)
        n = len(words)
        for i in range(n-1):
            s, d = words[i], words[i+1]
            if not self.compare(s, d, indict, outdict):
                return ""

        vocab = set()
        for word in words:
            vocab = vocab.union(set(word))

        return self.bfs_topological_sort(indict, outdict, vocab)

    # word1 and word2 is a valid comparsion.
    def compare(self, word1, word2, indict, outdict):
        # invalid order.
        if len(word1) > len(word2) and word1[:len(word2)] == word2:
            return False

        l = min(len(word1), len(word2))
        for i in range(l):
            a, b = word1[i], word2[i]
            if a == b:
                continue
            outdict[a].add(b)
            indict[b].add(a)
            # only record the first pair of different chars.
            break

        return True

    # bfs to sort graph
    def bfs_topological_sort(self, indict, outdict, vocab):
        q = []
        # find all vertex with 0 indegree.
        for c in vocab:
            if not indict[c]:
                q.append(c)

        # track the number of visited nodes.
        visited = 0
        ans = []
        while q:
            size = len(q)
            while size > 0:
                n = q.pop(0)
                size -= 1

                # record the topological order via bfs over graph.
                ans.append(n)

                # traverse to the neighbors
                if outdict[n]:
                    for m in outdict[n]:
                        # substract the in degree by 1
                        indict[m].remove(n)
                        # its in-degree becomes 0, put m into the queue.
                        if not indict[m]:
                            q.append(m)

                # records the number in ans.
                visited += 1

        if visited != len(vocab):
            return ""
        else:
            return "".join(ans)

s = Solution()
#print(s.alienOrder(["wrt","wrf","er","ett","rftt"]))
print(s.alienOrder(["za","zb","ca","cb"]))
