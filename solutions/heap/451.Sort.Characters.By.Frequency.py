import queue as q

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or s == "":
            return s

        char_freq = dict()
        for c in s:
            if c in char_freq.keys():
                char_freq[c] += 1
            else:
                char_freq[c] = 1
        # default is minHeap
        pq = q.PriorityQueue()
        for (k, v) in char_freq.items():
            pq.put((v, k))
        results = ""
        while not pq.empty():
            (v, k) = pq.get()
            # repeat k for v times
            for i in range(v):
                results += k
        # reverse the results for descending order
        return results[::-1]



def main():
    s = Solution()
    print(s.frequencySort("tree"))


if __name__ == "__main__":
    main()