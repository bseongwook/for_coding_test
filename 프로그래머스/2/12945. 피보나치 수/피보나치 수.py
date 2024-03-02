def solution(n):
    dp = [0] * (n+5)
    
    dp[1] = 1
    dp[2] = 1
    
    if n == 2:
        return 1
    else:
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] % 1234567