class FenwickTree: # (binary index tree)
    def __init__(self, n):
        self._sums = [0 for _ in range(n + 1)]

    # update the ith number with delta
    def update(self, i, delta):
        while i < len(self._sums):
            self._sums[i] += delta
            # lowbit
            i += i & -i

    # query the sum of the first i numbers'
    def query(self, i):
        s = 0
        while i > 0:
            s += self._sums[i]
            # lowbit
            i -= i & -i
        return s