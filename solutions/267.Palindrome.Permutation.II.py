class Solution:
    def generatePalindromes(self, s):
        """
        Given a string s, return all the palindromic permutations (without duplicates) of it.
        Return an empty list if no palindromic permutation could be form.

        Example 1:

        Input: "aabb"
        Output: ["abba", "baab"]
        Example 2:

        Input: "abc"
        Output: []

        :type s: str
        :rtype: List[str]

        Idea:
        1) calculate char frequency and if only 0/1 odd frequency char, remove one of that char to get a list of duplicated chars
        2) generate all unique permutations of that half list.
        3) combine the that char (if exists) with permtuations to generate all Palindromes.

        """
        if not s:
            return []
        cfreq = dict()
        for c in s:
            cfreq[c] = cfreq.get(c, 0) + 1
        odd_count = 0
        odd_char = None
        chars = []
        for c, f in cfreq.items():
            if f % 2 == 1:
                odd_count += 1
                odd_char = c
                chars += [c] * (cfreq[odd_char] // 2)
                if odd_count > 1:
                    return []
            else:
                chars += [c] * (cfreq[c] // 2)

        used = [False] * len(chars)
        permutation = []
        permutations= []
        self.dfs(chars, 0, len(chars), used, permutation,permutations)

        results = []
        for p in permutations:
            result = "".join(p + ([odd_char] if odd_char else []) + p[::-1])
            results.append(result)
        return results

    def dfs(self, chars, level, target_level, used, permutation, permutations):
        if level == target_level:
            permutations.append(permutation.copy())
            return
        else:
            handled = set()
            for i in range(len(chars)):
                if used[i]:
                    continue
                if chars[i] in handled:
                    continue
                used[i] = True
                handled.add(chars[i])
                permutation.append(chars[i])
                self.dfs(chars, level+1, target_level, used, permutation, permutations)
                permutation.pop()
                used[i] = False
            return

s = Solution()
print(s.generatePalindromes("aabacbabbcc"))