class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool

        Note that: circle means the robot returns to the original at the last step.

        """
        if moves is None or moves == "":
            return True
        x = 0
        y = 0
        for m in moves:
            if m == 'L':
                x -= 1
            elif m == 'R':
                x += 1
            elif m == 'U':
                y -= 1
            elif m == 'D':
                y += 1
        return (x, y) == (0, 0)
