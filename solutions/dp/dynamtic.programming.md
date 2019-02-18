# Dynmatic Programming

## Dynmatic Programming Template
    '''
    dp = new int[n + 1]
    for i = 1 to n:
      dp[i] = f(A[i], dp[i-1], dp[i-2], ...)
    return dp[n]
    '''

## When to use DP
* When recursion alone O(2^n) does not work. 
* Counting
* Optimization

## Requirments
* optimal substructure
* overlapping subproblems
* No-after affect

## Algorithm that use DP
* Fibonacci Sequence
* LCS
* Knapsack
* ....


## Template
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