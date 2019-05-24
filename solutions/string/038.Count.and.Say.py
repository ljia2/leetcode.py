class Solution:
    def countAndSay(self, n):
        """
        The count-and-say sequence is the sequence of integers with the first five terms as following:

        1.     1
        2.     11
        3.     21
        4.     1211
        5.     111221
        1 is read off as "one 1" or 11.
        11 is read off as "two 1s" or 21.
        21 is read off as "one 2, then one 1" or 1211.

        Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

        Note: Each term of the sequence of integers will be represented as a string.



        Example 1:

        Input: 1
        Output: "1"
        Example 2:

        Input: 4
        Output: "1211"
        
        :type n: int
        :rtype: str
        """

        if n == 1:
            return "1"

        pron = self.countAndSay(n-1)
        count = ""
        start = 0
        while start < len(pron):
            c = pron[start]
            freq = 1
            while start + 1 < len(pron) and pron[start+1] == pron[start]:
                freq += 1
                start += 1
            count += str(freq) + c
            start += 1
        return count

s = Solution()
print(s.countAndSay(6))





