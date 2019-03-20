class Solution:
    def totalFruit(self, tree):
        """
        In a row of trees, the i-th tree produces fruit with type tree[i].

        You start at any tree of your choice, then repeatedly perform the following steps:

        Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
        Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

        Note that you do not have any choice after the initial choice of starting tree:
        you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

        You have two baskets, and each basket can carry any quantity of fruit,
        but you want each basket to only carry one type of fruit each.

        What is the total amount of fruit you can collect with this procedure?


        Example 1:

        Input: [1,2,1]
        Output: 3
        Explanation: We can collect [1,2,1].
        Example 2:

        Input: [0,1,2,2]
        Output: 3
        Explanation: We can collect [1,2,2].
        If we started at the first tree, we would only collect [0, 1].
        Example 3:

        Input: [1,2,3,2,2]
        Output: 4
        Explanation: We can collect [2,3,2,2].
        If we started at the first tree, we would only collect [1, 2].
        Example 4:

        Input: [3,3,3,1,2,1,1,2,3,3,4]
        Output: 5
        Explanation: We can collect [1,2,1,1,2].
        If we started at the first tree or the eighth tree, we would only collect 4 fruits.


        Note:

        1 <= tree.length <= 40000
        0 <= tree[i] < tree.length
        :type tree: List[int]
        :rtype: int


        two pointer solution

        LC 1004.

        """
        s = e = 0
        ans = -1
        baskets = set()
        baskets.add(tree[s])
        while e < len(tree):
            # keep adding fruit into basket.
            if tree[e] in baskets or len(baskets) < 2:
                e += 1
                # a new fruit can be added into basket.
                if e < len(tree) and len(baskets) < 2:
                    baskets.add(tree[e])
            else:
                # a third typed fruit is encoutered and then stop; update # of fruit with a start of s.
                ans = max(e-s, ans)

                # how to find then next start
                baskets = set()
                baskets.add(tree[e])
                s = e
                while s > 0:
                    if tree[s-1] in baskets:
                        s -= 1
                    elif len(baskets) < 2:
                        baskets.add(tree[s-1])
                        s -= 1
                    else:
                        break
        # do not forget the last possible when existing while loop.
        return max(ans, e - s)

s = Solution()
#print(s.totalFruit([0,1,2,2]))
#print(s.totalFruit([1,2,3,2,2]))
print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))