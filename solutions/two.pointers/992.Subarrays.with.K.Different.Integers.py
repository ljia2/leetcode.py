import collections
class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        Given an array A of positive integers,
        call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

        (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

        Return the number of good subarrays of A.

        Example 1:
        Input: A = [1,2,1,2,3], K = 2
        Output: 7
        Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

        Example 2:
        Input: A = [1,2,1,3,4], K = 3
        Output: 3
        Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

        Note:
        1 <= A.length <= 20000
        1 <= A[i] <= A.length
        1 <= K <= A.length

        :type A: List[int]
        :type K: int
        :rtype: int

        1 <= A.length <= 20000 hints O(n) or O(nlogn).

        see leecode 159.

        two pointers, start and end.


        Intuition:
        Write a helper using sliding window,
        to get the number of subarrays with at most K distinct elements.
        Then f(exactly K) = f(atMost K) - f(atMost K-1).

        Of course, you can merge 2 for loop into ones, if you like.

        Time Complexity:
        O(N)

        How to define a function to find the # of subarray at most K integer?
        1) Find the maximum subarray l with K integers, then there are (l + 1) * l / 2 subarraies at most K intergers.


        """

        if K == 0 or not A:
            return 0

        return self.subarraysWithAtMostK(A, K) - self.subarraysWithAtMostK(A, K-1)

    def subarraysWithAtMostK(self, A, K):
        counter = collections.Counter()
        res = start = 0
        for end in range(len(A)):
            # use K to record how many distinct integers in counter
            if counter[A[end]] == 0:
                K -= 1

            # update counter
            counter[A[end]] += 1

            # when K < 0, the current window with K + 1 integers.
            # retreat start to make the window with K integers.
            while K < 0:
                counter[A[start]] -= 1
                if counter[A[start]] == 0:
                    K += 1
                start += 1

            # a window from start to end;
            # when K >= 0, it is with at most K integers.
            # it actually contribute end-start + 1 subarrys ending with end.
            res += end - start + 1
        return res

s = Solution()
#print(s.subarraysWithKDistinct([1,2,1,2,3], 2))
#print(s.subarraysWithKDistinct([1,2,1,3,4], 3))
print(s.subarraysWithKDistinct([2,1,1,1,2], 1))