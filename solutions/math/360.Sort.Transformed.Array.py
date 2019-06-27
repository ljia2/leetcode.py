from collections import deque

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        Given a sorted array of integers nums and integer values a, b and c.
        Apply a quadratic function of the form f(x) = ax^2 + b^x + c to each element x in the array.

        The returned array must be in sorted order (increasing).

        Expected time complexity: O(n)

        Example 1:

        Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
        Output: [3,9,15,33]
        Example 2:

        Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
        Output: [-23,-5,1,7]

        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]



        For ax2 + bx + c = 0, the values of x which are the solutions of the equation are given by:

        x = {-b +/- math.sqrt(b^2 - 4ac) } / 2a


        2ax + b = 0 -> x = -b/2a

        1) a > 0, two pointers of numbers by comparing the distance to x (x axis); the further the bigger.
        2) a < 0, two pointers of numbers by comparing the distance to x; the further the smaller

        """
        if not nums:
            return []

        if a == 0:
            ans = list(map(lambda x: b*x + c, nums))
            if b < 0:
                ans.reverse()
            return ans

        if a < 0:
            ans = self.sortTransformedArray(nums, -a, -b, -c)
            ans.reverse()
            return list(map(lambda x: -x, ans))

        ans = deque()
        t = -b / (2.0*a)
        i, j = 0, len(nums) - 1
        while i < j:
            di, dj = abs(nums[i] - t), abs(nums[j] - t)
            if di > dj:
                ans.appendleft(self.f(nums[i], a, b, c))
                i += 1
            else:
                ans.appendleft(self.f(nums[j], a, b, c))
                j -= 1

        # do not forget the last one when l == r.
        ans.appendleft(self.f(nums[i], a, b, c))

        return ans

    def f(self, x, a, b, c):
        return a*x*x + b*x + c


s = Solution()
print(s.sortTransformedArray([-4,-2,2,4], -1, 3, 5))