class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits:
            if digits[-1] < 9:
                digits[-1] += 1

            else:
                digits = self.plusOne(digits[:-1])
                digits.append(0)
            return digits
        else:
            return [1]


def main():
    s = Solution()
    results = s.plusOne([9, 9])
    print(results)


if __name__ == '__main__':
    main()