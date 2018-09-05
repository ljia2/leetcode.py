class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return "1"
        else:
            pron = self.countAndSay(n-1)
            count = ""
            start = 0
            while start < len(pron):
                c = pron[start]
                freq = 1
                while start < len(pron) - 1 and pron[start+1] == pron[start]:
                    freq += 1
                    start += 1
                count += str(freq) + c
                start += 1
            return count

s = Solution()
print(s.countAndSay(6))





