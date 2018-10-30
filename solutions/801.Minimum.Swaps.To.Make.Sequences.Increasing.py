class DPSolution:
    def minSwap(self, A, B):
        """
        We have two integer sequences A and B of the same non-zero length.

        We are allowed to swap elements A[i] and B[i].
        Note that both elements are in the same index position in their respective sequences.

        At the end of some number of swaps, A and B are both strictly increasing.
        (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

        Given A and B, return the minimum number of swaps to make both sequences strictly increasing.
        It is guaranteed that the given input always makes it possible.

        Example:
        Input: A = [1,3,5,4], B = [1,2,3,7]
        Output: 1
        Explanation:
        Swap A[3] and B[3].  Then the sequences are:
        A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
        which are both strictly increasing.

        Note:

        A, B are arrays with the same length, and that length will be in the range [1, 1000].
        A[i], B[i] are integer values in the range [0, 2000].

        :type A: List[int]
        :type B: List[int]
        :rtype: int

        swap[i] denotes the min swaps (to make A and B strictively increasing) with swapping A[i] and B[i]

        keep[i] denotes the min swaps (to make A and B strictively increasing) without swapping A[i] and B[i]

        Transition:

        1) A[i] > A[i-1] and B[i] > B[i-1]
            keep[i] = keep[i-1] # without swapping i
            swap[i] = swap[i-1] + 1 # swap both i-1 and i

        2) B[i] > A[i-1] and A[i] > B[i-1]
            keep[i] = min(keep[i], swap[i-1]) # swapping i-1 to guarantee strictly increasing
            swap[i] = min(swap[i], keep[i-1] + 1) # keeping i-1 and swapping i to gurantee stictly increase

        Note that case 1) and case 2) must either happens or both happens.

        If none of cases happens, there is not solutions.


        """
        # initialize swap and keep arraies
        swap = [len(A)+1] * len(A)
        keep = [len(A)+1] * len(B)
        # base case: swap A[0] and B[0] needs 1 swap; keep A[0] and B[0] needs 0 swap
        swap[0] = 1
        keep[0] = 0

        for i in range(1, len(A)):
            if A[i] > A[i-1] and B[i] > B[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1] + 1

            if B[i] > A[i-1] and A[i] > B[i-1]:
                keep[i] = min(keep[i], swap[i-1])
                swap[i] = min(swap[i], keep[i-1] + 1)

        return min(swap[-1], keep[-1])