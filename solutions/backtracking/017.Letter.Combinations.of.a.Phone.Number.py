# class Solution:
#     def __init__(self):
#         self.digit2chars = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
#
#     def letterCombinations(self, digits):
#         """
#         Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
#         A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#         Example:
#
#         Input: "23"
#         Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#         Note:
#
#         Although the above answer is in lexicographical order, your answer could be in any order you want
#         :type digits: str
#         :rtype: List[str]
#         """
#         if digits:
#             if len(digits) == 1:
#                 if digits[0] in self.digit2chars.keys():
#                     return [c for c in self.digit2chars.get(digits[0])]
#                 else:
#                     return []
#             else:
#                 return self.combine(self.letterCombinations(digits[0:1]), self.letterCombinations(digits[1:]))
#         else:
#             return []
#
#     def combine(self, chars, presults):
#         results = []
#         if presults and chars:
#             for c in chars:
#                 results.extend([c + r for r in presults])
#             return results
#         elif presults:
#             return presults
#         elif chars:
#             return chars
#         else:
#             return []


class DFSSolution:
    def __init__(self):
        self.digit2chars = {"0": "", "1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def letterCombinations(self, digits):
        """
        Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

        A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

        Example:

        Input: "23"
        Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
        Note:

        Although the above answer is in lexicographical order, your answer could be in any order you want
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        ans = []
        self.dfs(digits, 0, "", ans)
        return ans

    # recursive function must first write base cases
    def dfs(self, digits, start, comb, ans):
        if start == len(digits):
            ans.append(comb)
            return

        if digits[start] == "0" or digits[start] == "1":
            self.dfs(digits, start + 1, comb, ans)
        else:
            for c in self.digit2chars[digits[start]]:
                self.dfs(digits, start + 1, comb + c, ans)
        return

s = DFSSolution()
print(s.letterCombinations("223"))