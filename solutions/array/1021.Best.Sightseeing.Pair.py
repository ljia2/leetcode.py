class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot,
        and two sightseeing spots i and j have distance j - i between them.

        The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) :
        the sum of the values of the sightseeing spots, minus the distance between them.

        Return the maximum score of a pair of sightseeing spots.

        Example 1:

        Input: [8,1,5,2,6]
        Output: 11
        Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

        Note:

        2 <= A.length <= 50000
        1 <= A[i] <= 1000
        :type A: List[int]
        :rtype: int

        Explanation

        cur will record the best score that we have met.
        We iterate each value a in the array A,
        update res by max(res, cur + a)

        Also we can update cur by max(cur, a).
        Note that when we move forward,
        all sightseeing spot we have seen will be 1 distance further.

        So for the next sightseeing spot cur = Math.max(cur, a) **- 1**

        It's kinds of like, "A near neighbor is better than a distant cousin."

        Time Complexity:

        One pass, O(N) time, O(1) space
        """
        if not A or len(A) < 2:
            return None

        cur = res = 0
        for a in A:
            res = max(res, cur + a)
            cur = max(cur, a) - 1
        return res

s = Solution()
print(s.maxScoreSightseeingPair([8,1,5,2,6]))

