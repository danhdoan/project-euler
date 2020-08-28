with open('p081_matrix.txt', 'r') as f:
    a = list(map(lambda s: list(map(int, s.split(','))), \
            f.read().strip().split('\n')))

dp = [[0] * len(a[0]) for _ in range(len(a))]
dp[0][0] = a[0][0]
for i in range(1, len(dp)):
    dp[i][0] = a[i][0] + dp[i-1][0]

for j in range(1, len(dp[0])):
    dp[0][j] = a[0][j] + dp[0][j-1]

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        dp[i][j] = a[i][j] + min(dp[i-1][j], dp[i][j-1])

print(dp[len(dp)-1][len(dp[0])-1])
