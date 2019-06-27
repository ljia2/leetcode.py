import bisect


class Solution(object):
    def sortedSquares(self, A):
        """
        Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number,
        also in sorted non-decreasing order.

        Example 1:

        Input: [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        Example 2:

        Input: [-7,-3,2,3,11]
        Output: [4,9,9,49,121]


        Note:

        1 <= A.length <= 10000
        -10000 <= A[i] <= 10000
        A is sorted in non-decreasing order.
        :type A: List[int]
        :rtype: List[int]

        divide and conquer.
        """

        if not A:
            return []

        if len(A) == 1:
            return [A[0]**2]

        ans = []
        if A[0] >= 0:
            for a in A:
                ans.append(a*a)
        elif A[-1] <= 0:
            for a in A:
                ans.append(a*a)
            ans.reverse()
        else:
            # A[0] < 0 and A[-1]= > 0
            zidx = bisect.bisect_right(A, 0)
            lans = self.sortedSquares(A[:zidx])
            rans = self.sortedSquares(A[zidx:])

            # merge two squared arrays.
            l = r = 0
            while l < len(lans) and r < len(rans):
                if lans[l] < rans[r]:
                    ans.append(lans[l])
                    l += 1
                else:
                    ans.append(rans[r])
                    r += 1

            # NOTE!!! do not forget the remaining (either) array
            ans += lans[l:] if l < len(lans) else rans[r:]

        return ans




s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
print(s.sortedSquares([-7,-3,2,3,11]))


class IterativeSolution(object):
    def sortedSquares(self, A):
        """
        Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number,
        also in sorted non-decreasing order.

        Example 1:

        Input: [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        Example 2:

        Input: [-7,-3,2,3,11]
        Output: [4,9,9,49,121]


        Note:

        1 <= A.length <= 10000
        -10000 <= A[i] <= 10000
        A is sorted in non-decreasing order.
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return []

        if len(A) == 1:
            return [A[0]**2]

        ans = []
        if A[0] >= 0:
            for a in A:
                ans.append(a*a)
        elif A[-1] <= 0:
            for a in A:
                ans.append(a*a)
            ans.reverse()
        else:
            # A[0] < 0 and A[-1= > 0
            zidx = bisect.bisect_right(A, 0)
            lans = self.sortedSquares(A[:zidx])
            rans = self.sortedSquares(A[zidx:])
            # merge two squared arrays.
            l = r = 0
            while l < len(lans) and r < len(rans):
                if lans[l] < rans[r]:
                    ans.append(lans[l])
                    l += 1
                else:
                    ans.append(rans[r])
                    r += 1
            # do not forget the remaining (either) array
            if l < len(lans):
                ans += lans[l:]
            elif r < len(rans):
                ans += rans[r:]

        return ans