# import bisect
#
# class Solution: # TLE
#     def shortestSubarray(self, A, K):
#         """
#         Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
#
#         If there is no non-empty subarray with sum at least K, return -1.
#
#         Example 1:
#
#         Input: A = [1], K = 1
#         Output: 1
#         Example 2:
#
#         Input: A = [1,2], K = 4
#         Output: -1
#         Example 3:
#
#         Input: A = [2,-1,2], K = 3
#         Output: 3
#
#         :type A: List[int]
#         :type K: int
#         :rtype: int
#         """
#         presum2index = dict()
#         psum = 0
#         psums = []
#         min_length = len(A) + 1
#         for i in range(len(A)):
#             psum += A[i]
#             if psum >= K:
#                 length = i + 1
#                 if min_length > length:
#                     min_length = length
#
#             if not psums:
#                 presum2index[psum] = i
#                 bisect.insort_left(psums, psum)
#                 continue
#
#             target = psum - K
#             # find a psum <= target = psum - K
#             tindex = bisect.bisect_right(psums, target)
#             while tindex > 0:
#                 length = i - presum2index[psums[tindex-1]]
#                 if min_length > length:
#                     min_length = length
#                 tindex -= 1
#             presum2index[psum] = i
#             bisect.insort_left(psums, psum)
#
#         return min_length if min_length < len(A) + 1 else -1
#
#

from collections import deque

class Solution:
    def shortestSubarray(self, A, K):
        """
        Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

        If there is no non-empty subarray with sum at least K, return -1.

        Example 1:

        Input: A = [1], K = 1
        Output: 1
        Example 2:

        Input: A = [1,2], K = 4
        Output: -1
        Example 3:

        Input: A = [2,-1,2], K = 3
        Output: 3

        Note:

        1 <= A.length <= 50000
        -10 ^ 5 <= A[i] <= 10 ^ 5
        1 <= K <= 10 ^ 9


        :type A: List[int]
        :type K: int
        :rtype: int

        50000 hints for linear algorithm


        显然，我们会想到使用dp[i]记录sum(A[:i])，那么这道题就变成了，给定一个数组dp,找到一组i,j，使得dp[j]-dp[i]>=K，且j-i尽量小！
        数据长度达到50000，显然不能使用O(n^2)复杂度的方法，我们得想办法让i,j只走一遍
        用一个简单的示例来分析，设 A = [4,-1,2,3],，K = 5，那么dp = [0,4,3,5,8]，我们从dp数组的第2个数开始分析，（
        假设来了个-1，那么因为-1比0小，后面任意一个数val如若满足val-0>K,那么val+1也一定大于K，且-1所在的位置i显然能获得更优解，
        所以0这个位置就失去了意义），

        现在考虑示例，来了个4，我们发现4-0小于5，我们怎么对4进行处理呢，因为考虑到之后或许会出现一个足够大的数，比如9，那么4相对于0是更优的，但也有可能只来一个8，那么4就没作用了，所以先暂且保留观察。等到来了一个5以上的数，我们依次对保留的数（目前是0，4）进行判断得最优解。
        接下来来了个3，那么根据上面提到的论点，4将会被舍弃，但3比0要大，故此时0，3保留。
        然后来了个5，5-0>=5，故找到一组i,j，记录下来，然后判断 5-3>=5 ?如若确实大于，即再次找到一组i,j，若小于，则5保留（考虑到之后或许来了个10），依次类推

        建立一个队列记录保留数字，初始为0
        依次对dp中的数进行分析，如果dp[i] - dp[Q[0]] >= K，则记录一次i,j
        如果dp[i] < dp[Q[-1]]，则舍弃Q[-1]

        """
        if max(A) >= K:
            return 1

        # presums[i] stores the first i elements
        presums = [0] * (len(A) + 1)
        psum = 0
        for i in range(len(A)):
            psum += A[i]
            presums[i+1] = psum

        # 初始化队列
        Q = deque([0])
        min_length = float("inf")
        for i in range(1, len(presums)):
            # keep retracting Q to find the smallest subarray (if exists) ending at i but >= K
            while Q and presums[i] - presums[Q[0]] >= K:
                min_length = min(min_length, i - Q.popleft())

            # if a bigger presum is calculated, we can get rid of the latest psum > presum,
            # because if psum is used to generated the subarray (sum >= K), presum must be used to generate a shorter subarray (sum >= K).
            while Q and presums[i] < presums[Q[-1]]:
                Q.pop()
            Q.append(i)
        return min_length if min_length < float("inf") else -1

s = Solution()
print(s.shortestSubarray([2, -1, 2], 3))