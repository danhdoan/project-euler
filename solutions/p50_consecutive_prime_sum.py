MAXN = 1000000
sieve = [True] * MAXN

for i in range(2, MAXN//2 + 1):
    j = 2*i
    while j < MAXN:
        sieve[j] = False
        j += i

primes = []
for i in range(2, MAXN):
    if sieve[i]:
        primes.append(i)

dp = [0] + primes.copy()
for i in range(1, len(dp)):
    dp[i] += dp[i - 1]

ans = 0
mx_len = 0
for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        sm = dp[j+1] - dp[i]
        if sm >= MAXN: continue

        if sieve[sm] and mx_len < j - i + 1:
            ans = sm
            mx_len = j - i + 1
            print(ans, mx_len)

print(f'Answer: {ans} - Max length: {mx_len}')
