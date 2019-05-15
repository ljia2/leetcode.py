# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return False

class Solution(object):

    def firstBadVersion(self, n):
        """
        You are a product manager and currently leading a team to develop a new product.
        Unfortunately, the latest version of your product fails the quality check.
        Since each version is developed based on the previous version, all the versions after a bad version are also bad.

        Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
        which causes all the following ones to be bad.

        You are given an API bool isBadVersion(version) which will return whether version is bad.
        Implement a function to find the first bad version. You should minimize the number of calls to the API.

        Example:

        Given n = 5, and version = 4 is the first bad version.

        call isBadVersion(3) -> false
        call isBadVersion(5) -> true
        call isBadVersion(4) -> true

        Then 4 is the first bad version.
        :type n: int
        :rtype: int
        """
        if n <= 0:
            raise Exception("Invalid Input!")

        l = 1
        r = n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l

### If there are multiple machines, we can do logN(N) search.