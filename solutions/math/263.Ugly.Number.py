from heapq import heappop, heappush

# class Solution: # Memory Limit Exceeded
#     def isUgly(self, num):
#         """
#         Write a program to check whether a given number is an ugly number.
#
#         Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
#         Example 1:
#
#         Input: 6
#         Output: true
#         Explanation: 6 = 2 × 3
#         Example 2:
#
#         Input: 8
#         Output: true
#         Explanation: 8 = 2 × 2 × 2
#         Example 3:
#
#         Input: 14
#         Output: false
#         Explanation: 14 is not ugly since it includes another prime factor 7.
#
#         Note:
#
#         1 is typically treated as an ugly number.
#         Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
#
#         :type num: int
#         :rtype: bool
#         """
#
#         if num <= 0:
#             return False
#         else:
#             if num < 4:
#                 return True
#             else:
#                 ugly = [False] * (num + 1)
#                 ugly[1] = True
#                 ugly[2] = True
#                 ugly[3] = True
#                 for i in range(1, num+1, 1):
#                     if ugly[i]:
#                        if i * 2 < num + 1:
#                            ugly[i*2] = True
#                        if i * 3 < num + 1:
#                            ugly[i*3] = True
#                        if i * 5 < num + 1:
#                            ugly[i*5] = True
#                 return ugly[num]
#
# class Solution2: # Time Limit Exceeded
#     def isUgly(self, num):
#         """
#         Write a program to check whether a given number is an ugly number.
#
#         Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
#         Example 1:
#
#         Input: 6
#         Output: true
#         Explanation: 6 = 2 × 3
#         Example 2:
#
#         Input: 8
#         Output: true
#         Explanation: 8 = 2 × 2 × 2
#         Example 3:
#
#         Input: 14
#         Output: false
#         Explanation: 14 is not ugly since it includes another prime factor 7.
#
#         Note:
#
#         1 is typically treated as an ugly number.
#         Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
#
#         :type num: int
#         :rtype: bool
#         """
#
#         if num <= 0:
#             return False
#         else:
#             if num < 4:
#                 return True
#             else:
#                 ugly_nums = [1, 2, 3]
#
#                 unum = heappop(ugly_nums)
#                 while unum < num + 1:
#                     if 2*unum not in ugly_nums:
#                         heappush(ugly_nums, 2*unum)
#                     if 3*num not in ugly_nums:
#                         heappush(ugly_nums, 3*unum)
#                     if 5*unum not in ugly_nums:
#                         heappush(ugly_nums, 5*unum)
#                     unum = heappop(ugly_nums)
#                     if unum == num:
#                         return True
#                 return False

class Solution3:
    def isUgly(self, num):
        """
        Write a program to check whether a given number is an ugly number.

        Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

        Example 1:

        Input: 6
        Output: true
        Explanation: 6 = 2 × 3
        Example 2:

        Input: 8
        Output: true
        Explanation: 8 = 2 × 2 × 2
        Example 3:

        Input: 14
        Output: false
        Explanation: 14 is not ugly since it includes another prime factor 7.

        Note:

        1 is typically treated as an ugly number.
        Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].

        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        if num < 4:
            return True
        elif num % 2 == 0 and self.isUgly(num/2):
            return True
        elif num % 3 == 0 and self.isUgly(num/3):
            return True
        elif num % 5 == 0 and self.isUgly(num/5):
            return True
        else:
            return False
