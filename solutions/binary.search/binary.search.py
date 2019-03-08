class BinarySearch:
    # find the value satisfying f.
    def binary_search(l, r):
        while l < r:
            m = l + (r - l) // 2
            # f(m) is count the number satisfying the question.
            if f(m):
                return m    # if m is the answer

            if g(m):
                r = m              # new range [l, m)
            else:
                l = m + 1          # new range [m+1, r)
        return l               # or not found

\
    # find first index i: A[i] > val, similar to bisect_right
    def upper_bound(A, val, l, r):
        while l < r:
            m = (l + r) // 2
            if A[m] > val:
                r = m
            else:
                l = m + 1
        return l

    # find first index i A[i] >= x, similar bisect_left
    def lower_bound(A, val, l, r):
        while l < r:
            m = l + (r - l) // 2
            if A[m] >= val:
                r = m
            else:
                l = m + 1
        return l
