"""
美式⾜足球，每场可以得2，3，6或者1分，⽽而且得了了6分之后才能得1分。
给⼀一个分数求多少种取得的⽅方法。注意:如果是5分，[2, 3]和[3, 2]是不不同 的⽅方式。
不不算难的dp，掐着时间写完，⾯面试官说他⾃自⼰己看看code的对错 就好，⾃自⼰己⽬目测应该是做出来了了。


dp[n][0]: # ways of scoring n ending with 1 point
dp[n][1]: # ways of scoring n ending with 2 point
dp[n][2]: # ways of scoring n ending with 3 point
dp[n][3]: # ways of scoreing n ending with 6 point


dp[1][0] = 0
dp[2][1] = 1
dp[3][2] = 1
dp[6][3] = 1

if n > 1:
    dp[n][0] = dp[n-1][3]
if n > 2:
    dp[n][1] = sum(dp[n-2][0 .. 3])
if n > 3:
    dp[n][2] = sum(dp[n-3][0 .. 3])
if n > 6:
    dp[n][3] = sum(dp[n-6][0 .. 3])
"""