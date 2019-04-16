class Solution:
    def isHappy(self, n):
        """
        Write an algorithm to determine if a number is "happy".

        A happy number is a number defined by the following process:
        Starting with any positive integer, replace the number by the sum of the squares of its digits,
        and repeat the process until the number equals 1 (where it will stay),
        or it loops endlessly in a cycle which does not include 1.

        Those numbers for which this process ends in 1 are happy numbers.

        Example:

        Input: 19
        Output: true
        Explanation:
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1
        :type n: int
        :rtype: bool

        Earlier posts gave the algorithm but did not explain why it is valid mathematically,
        and this is what this post is about: present a "short" mathematical proof.

        First of all, it is easy to argue that starting from a number I, if some value - say a - appears again during the process after k steps,
        the initial number I cannot be a happy number. Because a will continuously become a after every k steps.

        Therefore, as long as we can show that there is a loop after running the process continuously, the number is not a happy number.

        There is another detail not clarified yet:
        For any non-happy number, will it definitely end up with a loop during the process?
        This is important, because it is possible for a non-happy number to follow the process endlessly while having no loop.

        To show that a non-happy number will definitely generate a loop,
        we only need to show that for any non-happy number, all outcomes during the process are bounded by some large but finite integer N.
        If all outcomes can only be in a finite set (2,N], and since there are infinitely many outcomes for a non-happy number,
        there has to be at least one duplicate, meaning a loop!

        Suppose after a couple of processes, we end up with a large outcome O_1 with D digits where D is kind of large, say D>=4,
        i.e., O_1 > 999 (If we cannot even reach such a large outcome, it means all outcomes are bounded by 999 ==> loop exists).

        We can easily see that after processing O_1, the new outcome O_2 can be at most 9^2*D < 100D, meaning that O_2 can have at most 2+d(D) digits,
        where d(D) is the number of digits D have.
        It is obvious that 2+d(D) < D. We can further argue that O_1 is the maximum (or boundary) of all outcomes afterwards.
        This can be shown by contradictory:
        Suppose after some steps, we reach another large number O_3 > O_1. This means we process on some number W <= 999 that yields O_3.
        However, this cannot happen because the outcome of W can be at most 9^2*3 < 300 < O1.
        """
        if n <= 0:
            return False

        explored = [n]
        next_num = self.next_num(n)
        while next_num != 1 and next_num not in explored:
            print(next_num)
            explored.append(next_num)
            next_num = self.next_num(next_num)
        return next_num == 1

    def next_num(self, num):
        next_num = 0
        while num > 0:
            next_num += (num % 10) ** 2
            num = num // 10
        return next_num
