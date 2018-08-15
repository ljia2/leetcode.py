class Solution:
    def __init__(self):
        self.digit2chars = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits:
            if len(digits) == 1:
                if digits[0] in self.digit2chars.keys():
                    return [c for c in self.digit2chars.get(digits[0])]
                else:
                    return []
            else:
                return self.combine(self.letterCombinations(digits[0:1]), self.letterCombinations(digits[1:]))
        else:
            return []

    def combine(self, chars, presults):
        results = []
        if presults and chars:
            for c in chars:
                results.extend([c + r for r in presults])
            return results
        elif presults:
            return presults
        elif chars:
            return chars
        else:
            return []

def main():
    s = Solution()

    results = s.letterCombinations("223")
    print(results)


if __name__ == '__main__':
    main()