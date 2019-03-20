class Solution:
    def numRescueBoats(self, people, limit):
        """
        The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

        Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

        Return the minimum number of boats to carry every given person.

        (It is guaranteed each person can be carried by a boat.)


        Example 1:

        Input: people = [1,2], limit = 3
        Output: 1
        Explanation: 1 boat (1, 2)
        Example 2:

        Input: people = [3,2,2,1], limit = 3
        Output: 3
        Explanation: 3 boats (1, 2), (2) and (3)
        Example 3:

        Input: people = [3,5,3,4], limit = 5
        Output: 4
        Explanation: 4 boats (3), (3), (4), (5)
        Note:

        1 <= people.length <= 50000
        1 <= people[i] <= limit <= 30000

        :type people: List[int]
        :type limit: int
        :rtype: int

        greedy:

        1) sort people by their weights.
        2) two pointers from lightest and heaviest to see whether two people can be in a boat.
         2.a) if people[r] + people[l] > limit: one boat is used for people r only, r -= 1
         2.b) if people[l] + people[r] <= limit; one boat for l and r. l += 1, r -= 1

        """
        people.sort()
        l = 0
        r = len(people) - 1
        ans = 0
        while l < r:
            if people[l] + people[r] <= limit:
                ans += 1
                l += 1
                r -= 1
            else:
                ans += 1
                r -= 1
        if l == r:
            ans += 1
        return ans

