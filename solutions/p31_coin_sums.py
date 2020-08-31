dp = [0] * 201
dp[0] = 1

coins = [1, 2, 5, 10, 20, 50, 100, 200]
for c in coins:
    for i in range(201):
        if i >= c:
            dp[i] += dp[i - c]

print(f'Answer: {dp[200]}')
    
