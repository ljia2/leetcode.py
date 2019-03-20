import bisect
import collections


class Solution(object):
    def canReorderDoubled(self, A):
        """
        Given an array of integers A with even length,
        return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

        Example 1:

        Input: [3,1,3,6]
        Output: false
        Example 2:

        Input: [2,1,2,6]
        Output: false
        Example 3:

        Input: [4,-2,2,-4]
        Output: true
        Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
        Example 4:

        Input: [1,2,4,16,8,4]
        Output: false


        Note:

        0 <= A.length <= 30000
        A.length is even
        -100000 <= A[i] <= 100000

        :type A: List[int]
        :rtype: bool

        rearrange array to ensure the odd position value is 2 * even position value.

        split into positive and negative.
        for positive, start with smallest v and see whether 2*v in positive or not.
        for negative, start with biggest v and see whether 2*v in negative or not.
        """
        pdict, plist, zero, ndict, nlist = self.split(A)
        if zero % 2 != 0 or len(plist) % 2 != 0 or len(nlist) % 2 != 0:
            return False
        return self.canRecorder(pdict, plist) and self.canRecorder(ndict, nlist)

    def split(self, A):
        zero = 0
        pos = dict()
        plist = []
        neg = dict()
        nlist = []
        for a in A:
            if a > 0:
                pos[a] = pos.get(a, 0) + 1
                bisect.insort_left(plist, a)
            elif a < 0:
                neg[a] = neg.get(a, 0) + 1
                bisect.insort_left(nlist, a)
            else:
                zero += 1
        nlist.reverse()
        return pos, plist, zero, neg, nlist

    def canRecorder(self, d, l):
        for n in l:
            if n not in d.keys():
                continue
            if 2*n in d.keys():
                d[n] -= 1
                if d[n] == 0:
                    del d[n]
                d[2*n] -= 1
                if d[2*n] == 0:
                    del d[2*n]
            else:
                return False

        return len(d.keys()) == 0


class BetterSolution(object):
    def canReorderDoubled(self, A):
        """
        Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

        Example 1:

        Input: [3,1,3,6]
        Output: false
        Example 2:

        Input: [2,1,2,6]
        Output: false
        Example 3:

        Input: [4,-2,2,-4]
        Output: true
        Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
        Example 4:

        Input: [1,2,4,16,8,4]
        Output: false


        Note:

        0 <= A.length <= 30000
        A.length is even
        -100000 <= A[i] <= 100000

        :type A: List[int]
        :rtype: bool


        """
        c = collections.Counter(A)
        for x in sorted(c, key=abs):
            if c[x] > c[2 * x]:
                return False
            c[2 * x] -= c[x]
        return True


s = BetterSolution()
# print(s.canReorderDoubled([4,-2,2,-4]))
# print(s.canReorderDoubled([4,-2,0, 2,-4]))
# print(s.canReorderDoubled([4,-2,0,0,2,-4]))
print(s.canReorderDoubled([4,-2,0,0,2,-4,1,2]))
#print(s.canReorderDoubled([2,1,2,1,1,1,2,2]))