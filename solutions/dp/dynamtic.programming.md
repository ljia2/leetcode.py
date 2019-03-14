# Dynamic Programming

## When to use DP
* When recursion alone O(2^n) does not work. 
* Counting
* Optimization

## Requirements
* optimal substructure
* overlapping subproblems
* No-after affect

## Algorithm that use DP
* Fibonacci Sequence
* LCS
* Knapsack
* ....


## General Template
    """
    dp = .....      # create dp array
                    # add padding if needed.
    
    dp[0][0] =    # init dp array 
                  # base case
                  
    for i ....
        for j ... 
           dp[i][j] = .... # transition
           
    return dp[n][m]
    
    """
##

## Dynamic Programming Cases:

### Case 1.1
* Input: O(n)
* dp[i] = (optimal) solution of a subproblem (A[0 -> i])
* dp[i] only depends on constant smaller problems
* Time O(n) and Space O(n) -> O(1)
* Template

        dp = [0] * n
        for i in 1 to n:
            dp[i] = fp(dp[i-1], dp[i-2], ....)
        return dp[n]
    
* Example 1: prefix sum

        dp[i] is sum of A[0 -> i]
        dp[i] = d[i-1] + A[i]
* LC 70

        dp[i] is the # of ways to i-th stairs
        dp[i] = dp[i-2] + dp[i-1]
* LC 198

        dp[i] is the max $ of robbing A[0 -> i]
        dp[i] = max(dp[i-2] + A[i], dp[i-1])

* LC 801: minimum swaps to make sequence increasing

        dp[i][0] is the minSwaps(A[0->i]) after swapping A[i] and B[i]
        dp[i][1] is the minSwaps(A[0->i]) without swapping A[i] and B[i]
        
* LC 790: Domino nd Tromino Tiling

        dp[i][0] is ways to tile i cols
        dp[i][1] is ways to tile i cols + 1 for 1st row
        dp[i][2] is ways to tile i cols + 1 for 2nd row
        
* LC 746: Min Cost climbing Stairs

        dp[i] is the min $ to i-th stairs
        dp[i] = min(dp[i-2] + A[i-2], dp[i-1] + A[i-1])

### Case 1.2
* Input: O(n)
* dp[i] = (optimal) solution of a subproblem (A[0 -> i])
* dp[i] depends on all smaller problems (dp[0], dp[1], ..., dp[i-1])
* Time O(n^2) and Space O(n)
* Template

        dp = [0] * n
        for i = 1 to n:
            for j = 1 to i-1:
                dp[i] = max/min(dp[i], f(dp[j]))
        return dp[i]
        
* LC 139 Wordbreak

        dp[i] wordbreak(A[0->i])
        dp[i] = any k s.t. (dp[0->k] and word(A[k+1->i]))
        
* LC 818: Race Car:
        dp[i][0] is min steps to reach i facing right
        dp[i][1] is min steps to reach i facing left
        
        for k in range(1, i+1):
            c = min(dp[k][0] + 2, dp[k][1] + 1)
            dp[i][0] = min(dp[i][0], dp[i-k][0] + c)
            dp[i][1] = min(dp[i][1], dp[i-k][1] + c)
            
### Case 1.3
* Input O(m) + O(n), two arrays or strings
* dp[i][j] is the opt solution of subproblem A[0->i] and B[0->i]
* dp[i][j] depends on constant smaller problems (dp[i-1][j-1], dp[i][j-1] dp[i-1][j])
* Time O(mn) and Space O(mn)
* Template
        
        dp = [[0] * m for _ in range(n)]
        for i = 1 to n:
            for j = 1 to m:
                dp[i][j] = f(dp[i-1][j-1], dp[i][j-1] dp[i-1][j])
                
* LC 72 and LC 712

### Case 1.4
* Input O(n)
* dp[i][j] is (opt) solution of subproblem A[i->j], a subarray of input, each subproblem depends O(n) smaller problems
* Time O(n^3) and Space O(n^2)
* Template

        dp = [[0] * m for _ in range(n)]
        for l = 1 to n # subproblem size
            for i = 1 to n - l + 1 # subproblem start
                j = i + l - 1
                for k = i to j:
                    dp[i][j] = max(dp[i][j], fp(dp[i][k], dp[k][j]))
        return dp[1][m]
        
* LC 312 Burst Ballons

        dp[i][j] = burstBallon(A[i->j])
        
        dp[i][j] = max(dp[i][k-1] + dp[k+1][j] + C(k))
        
* LC 664: strange printer

        dp[i][j] = min steps to print A[i->j]
        dp[i][j] = min(dp[i][k] + dp[k][j])


### Case 2.1 
* Input O(mn)
* dp[i][j] is sol of A[0->i][0->j], each subproblem depends on O(1) subproblem
* Time O(mn) and Spance O(mn) -> O(m)
* Template:

        dp = [[0] * m for _ in range(n)]
        for i = 1 to n:
            for j = 1 to m:
                dp[i][j] = f(dp[i][j-1] , dp[i-1][j])


* LC 62

       dp[i][j] is ways from A[0][0] to A[i][j]
       dp[i][j] = dp[i][j-1] + dp[i-1][j]
   
* LC 64 Minmum Path Sum (similar to LC 62)

### Case 2.2
* Input O(mn)
* dp[k][i][j] sol of A[0->i][0->j] after k steps, each subproblem depends on O(1) subproblems
* Time O(kmn) and Spance O(kmn) -> O(mn)
* Template:
        
        dp = new int[k][m][n]
        for k = 1 to K:
            for i = 1 to m:
                for j = 1 to n:
                   dp[k][i][j] = f(dp[k-1][i+/-di][j+/-dj]
        return dp[K][m][n] or g(dp[K]) # g verifies the state of A[m][n]
        
* LC 576: Out of Boundary Paths
* LC 688: Knight Probabilty in Chessboard
   
   
 
