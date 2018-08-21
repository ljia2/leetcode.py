import queue as q

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return None
        if k < 1:
            return None

        hp = []
        for num in nums:
            # maintain a heap of size k
            if len(hp) < k:
                q.heappush(hp, num)
            else:
                lnum = q.heappop()
                if lnum < num:
                    q.heappush(hp, num)
                else:
                    q.heappush(hp, lnum)
        return hp.heappop()