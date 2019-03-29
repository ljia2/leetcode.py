import collections

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        In a list of songs, the i-th song has a duration of time[i] seconds.

        Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

        Example 1:

        Input: [30,20,150,100,40]
        Output: 3
        Explanation: Three pairs have a total duration divisible by 60:
        (time[0] = 30, time[2] = 150): total duration 180
        (time[1] = 20, time[3] = 100): total duration 120
        (time[1] = 20, time[4] = 40): total duration 60
        Example 2:

        Input: [60,60,60]
        Output: 3
        Explanation: All three pairs have a total duration of 120, which is divisible by 60.


        Note:

        1 <= time.length <= 60000
        1 <= time[i] <= 500

        :type time: List[int]
        :rtype: int
        """

        if not time or len(time) < 2:
            return 0
        ans = 0
        mod_dict = dict()
        for t in time:
            tmod = t % 60
            target = (60 - tmod) if tmod > 0 else tmod
            if target in mod_dict.keys():
                ans += mod_dict[target]
            mod_dict[tmod] = mod_dict.get(tmod, 0) + 1
        return ans


s = Solution()
print(s.numPairsDivisibleBy60([30,20,150,100,40]))