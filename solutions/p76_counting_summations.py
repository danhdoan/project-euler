N = 101
dp = [[0]*N for _ in range(N)]

def calc(u, v):
    if dp[u][v] > 0: return dp[u][v]
    if u == 0:
        if v == 0: dp[u][v] = 1
        eles: dp[u][v] = 0
    else:
        if u > v:
            dp[u][v] = calc(u-1, v)
        else:
            dp[u][v] = calc(u-1, v) + calc(u, v-u)
    return dp[u][v]


ans = calc(99, 100)
print(f'Answer: {ans}')
