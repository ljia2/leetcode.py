import heapq
import collections

class Solution:
    def topKFrequent(self, words, k):
        """
        Given a non-empty list of words, return the k most frequent elements.

        Your answer should be sorted by frequency from highest to lowest.
        If two words have the same frequency, then the word with the lower alphabetical order comes first.

        Example 1:
        Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
        Output: ["i", "love"]
        Explanation: "i" and "love" are the two most frequent words.
        Note that "i" comes before "love" due to a lower alphabetical order.

        Example 2:
        Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
        Output: ["the", "is", "sunny", "day"]
        Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
        with the number of occurrence being 4, 3, 2 and 1 respectively.

        Note:
        You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
        Input words contain only lowercase letters.
        Follow up:
        Try to solve it in O(n log k) time and O(n) extra space.

        :type words: List[str]
        :type k: int
        :rtype: List[str]

        build a word frequency hashtable and use a max heap to pop top k terms

        """

        wf = collections.Counter(words)
        # note that when two words are frequency same, output by alphabetical order (ascending);
        # therefore use negative frequency, because when frequency ties, use words alphabetical order
        hp = [(-f, w) for (w, f) in wf.items()]
        # heapify is linear time.
        heapq.heapify(hp)
        results = heapq.nsmallest(k, hp)
        return list(map(lambda x: x[1], sorted(results)))


s = Solution()
print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 1))