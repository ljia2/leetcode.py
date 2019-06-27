class Solution(object):
    def numberToWords(self, num):
        """
        Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

        Example 1:

        Input: 123
        Output: "One Hundred Twenty Three"
        Example 2:

        Input: 12345
        Output: "Twelve Thousand Three Hundred Forty Five"
        Example 3:

        Input: 1234567
        Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
        Example 4:

        Input: 1234567891
        Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

        :type num: int
        :rtype: str

        We should parse from low to high every 3 digits.

        """
        # How to Initialize the hundreds, tens and ones.
        hundwords = ["Hundred", "Thousand", "Million", "Billion"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninty"]
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

        if num == 0:
            return "Zero"

        negative = False
        overflow = False
        # Trick: negative convert to positive, avoid the overflow.
        if num < 0:
            negative = True
            if num == -2**31 - 1:
                overflow = True
                num = -(num + 1)

        ans = []
        count = -1
        while num > 0:
            # take the last 3 digits
            hunds = num % 1000
            # remove the last 3 digits
            num = num // 1000

            # indicate whether we care count hundred, thousand, million or billion
            count += 1

            # no words
            if hunds == 0:
                continue

            # not the lowest three digits, add the proper unit for the 3 digits, thousand, million or billion
            if count > 0:
                ans.append(hundwords[count])

            # process the digits of from low to high significance
            # process the lowest two digits
            tens = hunds % 100
            # if tens is between 1 and 19.
            if 0 < tens < 20:
                ans.append(ones[tens])
            else:
                # like, 81 -> one eighty (will reverse later).
                if tens % 10 > 0:
                    ans.append(ones[tens % 10])
                if tens // 10 > 0:
                    ans.append(tens[tens // 10])

            # process the higher of the three digits, if it is bigger than 100.
            if hunds // 100 > 0:
                # always use hundred if hunds > 100.
                ans.append(hundwords[0])
                ans.append(ones[hunds // 100])

        if negative:
            ans.append("Negative")

        ans.reverse()

        if overflow:
            ans.pop()
            ans.append("Eight")

        return " ".join(ans)


s = Solution()
print(s.numberToWords(1234567891))
print(s.numberToWords(-2**31-1))
print(s.numberToWords(2**31-1))