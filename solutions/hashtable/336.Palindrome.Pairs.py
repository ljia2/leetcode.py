class TrieNode:
    def __init__(self):
        self.dic = dict()
        self.index = None

class Solution(object):

    def palindromePairs(self, words):
        """
        Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
        so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

        Example 1:

        Input: ["abcd","dcba","lls","s","sssll"]
        Output: [[0,1],[1,0],[3,2],[2,4]]
        Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
        Example 2:

        Input: ["bat","tab","cat"]
        Output: [[0,1],[1,0]]
        Explanation: The palindromes are ["battab","tabbat"]

        :type words: List[str]
        :rtype: List[List[int]]

        The basic idea is to check each word for prefixes (and suffixes) that are themselves palindromes.
        If you find a prefix that is a valid palindrome,
        then the suffix reversed can be paired with the word in order to make a palindrome.
        It's better explained with an example.

        words = ["bot", "t", "to"]
        Starting with the string "bot". We start checking all prefixes. If "", "b", "bo", "bot" are themselves palindromes.
        The empty string and "b" are palindromes. We work with the corresponding suffixes ("bot", "ot")
        and check to see if their reverses ("tob", "to") are present in our initial word list.
        If so (like the word to"to"), we have found a valid pairing where the reversed suffix can be prepended
        to the current word in order to form "to" + "bot" = "tobot".

        You can do the same thing by checking all suffixes to see if they are palindromes.
        If so, then finding all reversed prefixes will give you the words that can be appended to the current word to form a palindrome.

        The process is then repeated for every word in the list. Note that when considering suffixes,
        we explicitly leave out the empty string to avoid counting duplicates.
        That is, if a palindrome can be created by appending an entire other word to the current word,
        then we will already consider such a palindrome when considering the empty string as prefix for the other word.
        """


        
