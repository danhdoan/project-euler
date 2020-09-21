N = 100
sieve = [True] * (N + 1)

for i in range(2, N//2+1):
    if sieve[i]:
        for j in range(2*i, N+1, i):
            sieve[j] = False

primes = []
for i in range(2, N+1):
    if sieve[i]: primes.append(i)

dp = [0] * (N+1)
dp[0] = 1
for p in primes:
    for i in range(p, N+1):
        dp[i] += dp[i-p]

for i, w in enumerate(dp):
    if w > 5000:
        print(i)
        break
