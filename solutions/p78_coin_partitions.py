N = 100001
dp = [0] * N

dp[0] = 1
for u in range(1, N):
    for v in range(u, N):
        dp[v] += dp[v - u]

    if u % 10000 == 0: 
        print(f'u: {u}')
    if dp[u] % 1000000 == 0:
        print(u)
        break
