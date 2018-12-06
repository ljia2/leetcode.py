class Solution:
    def fallingSquares(self, positions):
        """

        On an infinite number line (x-axis), we drop given squares in the order they are given.

        The i-th square dropped (positions[i] = (left, side_length)) is a square with the left-most point being positions[i][0] and sidelength positions[i][1].

        The square is dropped with the bottom edge parallel to the number line, and from a higher height than all currently landed squares.
        We wait for each square to stick before dropping the next.

        The squares are infinitely sticky on their bottom edge, and will remain fixed to any positive length surface they touch (either the number line or another square).
        Squares dropped adjacent to each other will not stick together prematurely.

        Return a list ans of heights. Each height ans[i] represents the current highest height of any square we have dropped, after dropping squares represented by positions[0], positions[1], ..., positions[i].

        Example 1:

        Input: [[1, 2], [2, 3], [6, 1]]
        Output: [2, 5, 5]
        Explanation:

        After the first drop of positions[0] = [1, 2]:
        _aa
        _aa
        -------
        The maximum height of any square is 2.


        After the second drop of positions[1] = [2, 3]:
        __aaa
        __aaa
        __aaa
        _aa__
        _aa__
        --------------
        The maximum height of any square is 5.
        The larger square stays on top of the smaller square despite where its center
        of gravity is, because squares are infinitely sticky on their bottom edge.


        After the third drop of positions[1] = [6, 1]:
        __aaa
        __aaa
        __aaa
        _aa
        _aa___a
        --------------
        The maximum height of any square is still 5.

        Thus, we return an answer of [2, 5, 5].


        Example 2:

        Input: [[100, 100], [200, 100]]
        Output: [100, 100]
        Explanation: Adjacent squares don't get stuck prematurely - only their bottom edge can stick to surfaces.
        Note:

        1 <= positions.length <= 1000.
        1 <= positions[i][0] <= 10^8.
        1 <= positions[i][1] <= 10^6.

        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if not positions:
            return []

        ans = []
        # store non-overlapping intervals
        squares = []
        # store non-overlapping interval 2 their heights
        square2height = dict()
        for position in positions:
            start, width = position
            end = start + width - 1
            if not squares:
                squares.append((start, end))
                square2height[(start, end)] = width
            else:
                nsquares = []
                nsquare2height = dict()
                # whether position overlap with a square
                insert = False
                for square in squares:
                    s, e = square

                    if s > end and not insert:
                        if (start, end) not in nsquares:
                            nsquares.append((start, end))
                            nsquare2height[(start, end)] = width
                        else:
                            nsquare2height[(start, end)] = max(nsquare2height[(start, end)], width)
                        insert = True

                    if e < start or s > end:
                        nsquares.append((s, e))
                        nsquare2height[(s, e)] = square2height[(s, e)]
                    else:
                        # situation 1: position is fully covered by square
                        if s < start and end < e:
                            nsquares.append((s, start))
                            nsquare2height[(s, start)] = square2height[square]

                            nsquares.append((start, end))
                            nsquare2height[(start, end)] = square2height[square] + width
                            insert = True

                            nsquares.append((end, e))
                            nsquare2height[(end, e)] = square2height[square]

                        # situation 2: square and position overlaps but square is on the left of position
                        elif s < start and e <= end:
                            nsquares.append((s, start))
                            nsquare2height[(s, start)] = square2height[square]

                            nsquares.append((start, end))
                            nsquare2height[(start, end)] = square2height[square] + width
                            insert = True
                        # situation 3: position fully covers square
                        elif start <= s and e <= end:
                            if (start, end) not in nsquares:
                                nsquares.append((start, end))
                                nsquare2height[(start, end)] = square2height[square] + width
                            else:
                                nsquare2height[(start, end)] = max(nsquare2height[(start, end)], square2height[square] + width)
                            insert = True
                        # situation 4: position and square overlaps but position is on the left of square
                        elif start <= s and end < e:
                            if (start, end) not in nsquares:
                                nsquares.append((start, end))
                                nsquare2height[(start, end)] = square2height[square] + width
                            else:
                                nsquare2height[(start, end)] = max(nsquare2height[(start, end)], square2height[square] + width)
                            insert = True
                            nsquares.append((end, e))
                            nsquare2height[(end, e)] = square2height[square]

                if not insert:
                    nsquares.append((start, end))
                    nsquare2height[(start, end)] = width

                squares = nsquares.copy()
                square2height = nsquare2height.copy()

            max_height = -1
            for height in square2height.values():
                max_height = max(max_height, height)
            ans.append(max_height)
        return ans

s = Solution()
print(s.fallingSquares([[1, 2], [2, 3], [6, 1]]))
print(s.fallingSquares([[6,1],[9,2],[2,4]]))