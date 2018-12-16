from collections import defaultdict
class Solution:
    def wordsAbbreviation(self, dict):
        """
        Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

        Begin with the first character and then the number of characters abbreviated, which followed by the last character.

        If there are any conflict, that is more than one words share the same abbreviation,
        a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique.
        In other words, a final abbreviation cannot map to more than one original words.
        If the abbreviation doesn't make the word shorter, then keep it as original.

        Example:

        Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
        Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]

        Note:
        Both n and the length of each word will not exceed 400.
        The length of each word is greater than 1.
        The words consist of lowercase English letters only.
        The return answers should be in the same order as the original array

        :type dict: List[str]
        :rtype: List[str]
        """

        word2index = defaultdict()
        for word in dict:
            word2index[word] = len(word2index.keys())

        abbr2words = defaultdict(list)
        for word in dict:
            abbr = self.default_abbr(word)
            abbr2words[abbr].append(word)

        abbr2words2 = defaultdict()
        for abbr in abbr2words:
            if len(abbr2words[abbr]) > 1:
                self.calc_abbr(abbr2words[abbr], abbr2words2)

        ans = [None] * len(dict)
        for abbr, words in abbr2words.items():
            if len(words) > 1:
                continue
            index = word2index[words[0]]
            ans[index] = abbr

        for abbr, word in abbr2words2.items():
            index = word2index[word]
            ans[index] = abbr
        return ans

    def default_abbr(self, word):
        if len(word) <= 3:
            return word
        return word[0] + str(len(word)-2) + word[-1]

    def calc_abbr(self, words, ans):
        handled = dict()
        for i in range(2, len(words[0])):
            prefix2index = defaultdict(list)
            for j in range(len(words)):
                if words[j] in handled.keys():
                    continue
                prefix = words[j][:i]
                prefix2index[prefix].append(words[j])

            for prefix in prefix2index.keys():
                if len(prefix2index[prefix]) == 1:
                    word = prefix2index[prefix][0]
                    abbr = prefix + str(len(word) - len(prefix) - 1) + word[-1]
                    if len(abbr) < len(word):
                        ans[abbr] = word
                        handled[word] = 1
        for j in range(len(words)):
            word = words[j]
            if word not in handled.keys():
                ans[word] = word
        return

s = Solution()
print(s.wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]))
print(s.wordsAbbreviation(["abcdefg","abccefg","abcckkg"]))