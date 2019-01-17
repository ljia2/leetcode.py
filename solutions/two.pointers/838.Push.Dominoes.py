class Solution:
    def pushDominoes(self, dominoes):
        """
        There are N dominoes in a line, and we place each domino vertically upright.

        In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

        https://leetcode.com/problems/push-dominoes/description/

        After each second, each domino that is falling to the left pushes the adjacent domino on the left.
        Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
        When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

        For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

        Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left;
        S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

        Return a string representing the final state.

        Example 1:

        Input: ".L.R...LR..L.."
        Output: "LL.RR.LLRRLL.."

        Example 2:

        Input: "RR.L"
        Output: "RR.L"

        Explanation: The first domino expends no additional force on the second domino.

        Note:
        0 <= N <= 10^5
        String dominoes contains only 'L', 'R' and '.

        :type dominoes: str
        :rtype: str

        -- each iteration of a second when a domino fails or not.

        state = initial state

        while True:
           next_state = dominoes_expansion(state)

           if next_state == state:
                break
           state = next_state
        return state
        """
        if len(dominoes) < 2:
            return dominoes

        state = dominoes
        while True:
            next_state = self.domino_fall(state)
            if next_state == state:
                break
            state = next_state
        return state

    def domino_fall(self, dominoes):
        new_dominoes = []
        for i, d in enumerate(dominoes):
            if d != '.':
                new_dominoes.append(d)
                continue

            if i == 0:
                if dominoes[i+1] == 'L':
                    new_dominoes.append(dominoes[i+1])
                else:
                    new_dominoes.append(d)
            elif i == len(dominoes) - 1:
                if dominoes[i-1] == 'R':
                    new_dominoes.append(dominoes[i-1])
                else:
                    new_dominoes.append(d)
            else:
                if dominoes[i-1] == dominoes[i+1]:
                    # L.L, R.R, ...
                    new_dominoes.append(dominoes[i-1])
                else:
                    # ..L
                    if dominoes[i-1] == '.' and dominoes[i+1] == 'L':
                        new_dominoes.append(dominoes[i+1])
                    # R..
                    elif dominoes[i+1] == '.' and dominoes[i-1] == 'R':
                        new_dominoes.append(dominoes[i-1])
                    else:
                        # L.R, R.L
                        new_dominoes.append(d)
        return ''.join(new_dominoes)

s = Solution()
print(s.pushDominoes(".L.R...LR..L.."))