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

def main():
    s = Solution()
    print(s.topKFrequent([1,1,1,2,2,3], 2))

if __name__ == "__main__":
    main()