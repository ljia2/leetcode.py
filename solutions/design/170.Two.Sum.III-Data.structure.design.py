class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sum = set()
        self.nums = []

    # O(n^2)
    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if self.nums:
            for num in self.nums:
                new_sum = num + number
                if new_sum not in self.sum:
                    self.sum.add(new_sum)
        self.nums.append(number)

    # O(1)
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        return value in self.sum

# use hashtable
class TwoSumII:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = dict()

    # O(1)
    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number not in self.nums.keys():
            self.nums[number] = 1
        else:
            self.nums[number] += 1

    # O(n)
    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if sum(self.nums.values()) < 2:
            return False
        else:
            for num in self.nums.keys():
                target = value - num
                if target != num and target in self.nums.keys():
                    return True
                elif target == num and self.nums[num] > 1:
                    return True
            return False

obj = TwoSumII()
obj.add(0)
print(obj.find(0))