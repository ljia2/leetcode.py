class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n is None or n == 0:
            return []
        if k == 0 or k > n:
            return []
        if k == 1:
            return [[i+1] for i in range(n)]
        else:
            n_set = [i+1 for i in range(n)]
            res1 = self.combine_set(n_set[1:], k-1)
            for r in res1:
                r.append(n_set[0])
            res2 = self.combine_set(n_set[1:], k)
            return res1 + res2

    def combine_set(self, n_set, k):
        if n_set is None or not n_set:
            return []
        if k == 0 or k > len(n_set):
            return []
        if k == 1:
            return [[i] for i in n_set]
        else:
            res1 = self.combine_set(n_set[1:], k-1)
            for r in res1:
                r.append(n_set[0])
            res2 = self.combine_set(n_set[1:], k)
            return res1 + res2


def main():
    s = Solution()
    print(s.combine(4, 2))


if __name__ == "__main__":
    main()