class Solution:
    def kSimilarity(self, A, B):
        """
        Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A
        exactly K times so that the resulting string equals B.

        Given two anagrams A and B, return the smallest K for which A and B are K-similar.

        Example 1:
        Input: A = "ab", B = "ba"
        Output: 1

        Example 2:
        Input: A = "abc", B = "bca"
        Output: 2

        Example 3:
        Input: A = "abac", B = "baca"
        Output: 2

        Example 4:
        Input: A = "aabc", B = "abca"
        Output: 2
        Note:

        1 <= A.length == B.length <= 20
        A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}

        :type A: str
        :type B: str
        :rtype: int
        """
        if A == B:
            return 0

        qe = [A]
        visited = set()
        visited.add(A)
        changes = 0
        while qe:
            size = len(qe)
            while size > 0:
                word = qe.pop(0)
                size -= 1

                if word == B:
                    return changes

                for w in self.swap_words(word, B):
                    if w in visited:
                        continue
                    qe.append(w)
                    visited.add(w)
            changes += 1
        return -1

    def swap_words(self, word, B):
        for i in range(len(word)):
            if word[i] == B[i]:
                continue
            start = i
            break
        swords = set()
        for j in range(start+1, len(word)):
            # skip non-necessary swap
            if word[j] != B[i]:
                continue
            sword = list(word)
            sword[i], sword[j] = sword[j], sword[i]
            swords.add("".join(sword))
        return swords

s = Solution()
print(s.kSimilarity("ab", "ba"))