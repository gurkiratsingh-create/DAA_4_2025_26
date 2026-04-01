def fib(n,dp):
    while n <= i:
        if n <= 1:
            dp[0]=0
            dp[1]=1
            n=2
        elif dp[n]==-1:
            return dp[n]
        else:
            dp[n] = dp[n-1] + dp[n-2]
        n += 1
    return dp[i-1]
n=0
i=5
dp =[-1] * (i+1)
print(fib(n,dp))