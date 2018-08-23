class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.abbr_dict = dict()
        for word in dictionary:
            if len(word) < 3:
                abbr = word
            else:
                abbr = word[0] + str(len(word)-2) + word[-1]
            if abbr not in self.abbr_dict.keys():
                # can not directly set(word), since str is treated as list, such an operation will convert str to set of characters
                self.abbr_dict[abbr] = set()
            self.abbr_dict[abbr].add(word)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
        1) empty abbr_dict, return True for all inputs
        2)
        """
        if len(word) < 3:
            abbr = word
        else:
            abbr = word[0] + str(len(word)-2) + word[-1]
        if abbr not in self.abbr_dict.keys():
            return True
        elif len(self.abbr_dict[abbr]) == 1 and word in self.abbr_dict[abbr]:
            return True
        return False

# Your ValidWordAbbr object will be instantiated and called as such:
obj = ValidWordAbbr(["hello", "hll3o"])
param_1 = obj.isUnique("hello")