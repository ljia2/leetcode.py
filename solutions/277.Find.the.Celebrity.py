# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

        Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

        You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n), your function should minimize the number of calls to knows.

        Note: There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

        :type n: int
        :rtype: int

        for each person a: find out whether a is celeberity
            is_cele = True
            for each person b (not a):
                 is_cele &= !know(a, b) and knows(b, a)

        Speedup: is b knows a, b must not be a celebrity.

        Everytime, there is a person added into non-celebrity.
        T: O(n)
        S: O(n)

        """
        if n <= 0:
            return 0

        non_celeberity = []
        for i in range(n):
            if i in non_celeberity:
                continue

            is_celebrity = True
            for j in range(n):
                if j == i:
                    continue

                if not knows(i, j) and knows(j, i):
                    non_celeberity.append(j)
                else:
                    non_celeberity.append(i)
                    is_celebrity = False
                    break
            if is_celebrity:
                return i
        return -1



