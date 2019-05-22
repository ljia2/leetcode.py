import queue as q

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0 or k <= 0:
            return []
        nfreq = dict()
        for num in nums:
            if num in nfreq.keys():
                nfreq[num] += 1
            else:
                nfreq[num] = 1
        pq = q.PriorityQueue()
        for (key, val) in nfreq.items():
            pq.put((len(nums) - val, key))
        results = []
        while not pq.empty() and k > 0:
            _, key = pq.get()
            results.append(key)
            k -= 1
        return results

### Can you do it in O(n) time complexity
import random
import collections

class QuickSelectSolution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        # Approach 4: Quick Select
        # Steps:
        # 1. Get the counts using collections.counter
        # 2. Do a quick select on the counts list using n - k as K,
        #    Thus, converting kth smallest to kth largest
        # 3. Now we'll have the elements after n - kth positing all having k largest frequencies
        # 4. Return the actual elements from those items

        # Time: O(n), Avg case due to randomization
        # Space: O(1)
        """
        counts = list(collections.Counter(nums).items())
        n = len(counts)
        print(counts)
        self.quick_select(counts, 0, n - 1, n - k)
        return [x[0] for x in counts[n - k:]]

    def quick_select(self, nums, l, r, K):
        if l == r:
            return

        mid = self.rand_partition(nums, l, r)

        if K < mid:
            self.quick_select(nums, l, mid - 1, K)
        elif K > mid:
            self.quick_select(nums, mid + 1, r, K)
        else:
            return

    def rand_partition(self, nums, l, r):
        i = random.randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return self.partition(nums, l, r)

    def partition(self, nums, l, r):
        i = l - 1
        pivot = nums[r][1]
        for j in range(l, r):
            if nums[j][1] > pivot:
                continue
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

def main():
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3], 2))

if __name__ == "__main__":
    main()