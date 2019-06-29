import bisect
import collections

class Solution(object):
    def reconstructQueue(self, people):
        """
        Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
        where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h.
        Write an algorithm to reconstruct the queue.

        Note:
        The number of people is less than 1,100.

        Example

        Input:
        [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

        Output:
        [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

        :type people: List[List[int]]
        :rtype: List[List[int]]



        1. Pick out tallest group of people and sort them in a subarray (S).
           Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
        2. For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
        """

        if not people or len(people) == 1:
            return people

        h2k = collections.defaultdict(list)
        for h, k in people:
            bisect.insort_right(h2k[h], k)

        heights = list(h2k.keys())
        heights.sort(reverse=True)

        ans = []
        for h in heights:
            for k in h2k[h]:
                bisect.insort_left(ans, (k, h))

        return list(map(lambda x: [x[1], x[0]], ans))


s = Solution()
print(s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))