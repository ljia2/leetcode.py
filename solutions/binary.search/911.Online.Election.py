"""
In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function:
TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.

Votes cast at time t will count towards our query.
In the case of a tie, the most recent vote (among tied candidates) wins.

Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation:
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.


Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0].
"""

import bisect

class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """

        self.winners = []
        self.times = times
        p2count = dict()
        max_p = -1
        for i, t in enumerate(times):
            p = persons[i]
            if max_p < 0:
                max_p = p
                p2count[p] = 1
            else:
                c = p2count.get(p, 0)
                if p == max_p:
                    p2count[p] = c + 1
                else:
                    if c + 1 < p2count[max_p]:
                        p2count[p] = c+1
                    else:
                        max_p = p
                        p2count[p] = c+1
            self.winners.append(max_p)


    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        i = bisect.bisect_right(self.times, t)
        if i > 0:
            return self.winners[i-1]
        else:
            raise RuntimeError("""time $t is invalid! """)


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)

obj = TopVotedCandidate([0,0,0,0,1],[0,6,39,52,75])
obj.q(99)