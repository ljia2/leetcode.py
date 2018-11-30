class SegmentTreeSolution:
    def countSmaller(self, nums):
        """
        You are given an integer array nums and you have to return a new counts array.
        The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

        Example:

        Input: [5,2,6,1]
        Output: [2,1,1,0]
        Explanation:
        To the right of 5 there are 2 smaller elements (2 and 1).
        To the right of 2 there is only 1 smaller element (1).
        To the right of 6 there is 1 smaller element (1).
        To the right of 1 there is 0 smaller element.

        :type nums: List[int]
        :rtype: List[int]

        Convert to frequecy distribution (the original problem becomes sumRange) and then use segment tree to speed up)

        T: O(nlogn)
        S: O(n)

        """
        # get all unique nums in assending order
        unums = sorted(set(nums))
        # record each unique num's sorted index in nums
        num2index = dict()
        for num in unums:
            if num not in num2index.keys():
                num2index[num] = len(num2index) + 1

        # a list to store each unique element's frequency in nums.
        # freq[0] = 0,
        # freq[1] is the frequency of the smallest unique number in nums
        # freq[2] is the frequency of the second smallest unique number in nums
        freq = [0] * (len(nums) + 1)

        # build up a segment tree based on frequency
        stree = self.buildSegmentTree(freq)

        results = []
        # iterate nums from tail, update its frequency and then sumFrequency (via Segment Tree) of those elements less than it.
        for i in range(len(nums)-1, -1, -1):
            index = num2index[nums[i]]
            self.updateTree(stree, index)
            # summing up the frequency of those elements less than nums[i] and succeed nums[i[
            results.append(self.sumFrequency(stree, index-1))
        # reverse order of results, since the iteration from tail.
        results.reverse()
        return results

    def buildSegmentTree(self, freq):
        size = len(freq)
        # segment tree, the second half storing the original freq,
        # the first half tree[i] = tree[2*i] + tree[2*i + 1] where i > 0
        tree = [0] * size + freq

        for i in range(size-1, 0, -1):
            tree[i] = tree[2*i] + tree[2*i+1]
        return tree

    def updateTree(self, tree, index):
        tindex = len(tree) // 2 + index
        tree[tindex] += 1
        while tindex > 0:
            parent_tindex = tindex // 2
            if tindex % 2 == 0:
                tree[parent_tindex] = tree[tindex] + tree[tindex+1]
            else:
                tree[parent_tindex] = tree[tindex-1] + tree[tindex]
            tindex = parent_tindex

    def sumFrequency(self, stree, index):
        # sum the range from ti to tj (both inclusive)
        ti = 0 + len(stree) // 2
        tj = index + len(stree) // 2

        result = 0
        while ti <= tj:
            if ti % 2 != 0:
                result += stree[ti]
                ti += 1

            if tj % 2 != 1:
                result += stree[tj]
                tj -= 1
            ti //= 2
            tj //= 2
        return result


s = SegmentTreeSolution()
print(s.countSmaller([5, 2, 6, 1]))

class BinarySearchTreeSolution:
    def countSmaller(self, nums):
        """
        You are given an integer array nums and you have to return a new counts array.
        The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

        Example:

        Input: [5,2,6,1]
        Output: [2,1,1,0]
        Explanation:
        To the right of 5 there are 2 smaller elements (2 and 1).
        To the right of 2 there is only 1 smaller element (1).
        To the right of 6 there is 1 smaller element (1).
        To the right of 1 there is 0 smaller element.

        :type nums: List[int]
        :rtype: List[int]

        Convert to frequency distribution (the original problem becomes sumRange) and then use binary search tree to speed up)

        T: O(nlogn)
        S: O(n)

        """
        # get all unique nums in increasing order
        unums = sorted(set(nums))
        # record each unique numbers' sorted index in nums
        num2index = dict()
        for num in unums:
            if num not in num2index.keys():
                num2index[num] = len(num2index) + 1

        # a list to store each unique element's frequency in nums.
        # freq[0] = 0,
        # freq[1] is the frequency of the smallest unique number in nums
        # freq[2] is the frequency of the second smallest unique number in nums
        bistree = [0] * (len(nums) + 1)

        results = []
        # iterate nums from tail, update its frequency and then sumFrequency (via Segment Tree) of those elements less than it.
        for i in range(len(nums)-1, -1, -1):
            index = num2index[nums[i]]
            self.update(bistree, index, 1)
            # summing up the frequency of those elements less than nums[i] and succeed nums[i[
            results.append(self.query(bistree, index-1))

        # reverse order of results, since the iteration from tail.
        results.reverse()
        return results

    def update(self, tree, index, delta):
        ti = index + 1
        while ti < len(tree):
            tree[ti] += delta
            ti += ti & -ti

    def query(self, tree, index):
        s = 0
        ti = index + 1
        while ti > 0:
            s += tree[ti]
            ti -= ti & -ti
        return s


s = BinarySearchTreeSolution()
print(s.countSmaller([5, 2, 6, 1]))

