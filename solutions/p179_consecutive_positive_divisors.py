N = 10**7
sieve = [2] * (N + 1)
for i in range(2, N // 2 + 1):
    j = 2*i
    while j <= N:
        sieve[j] += 1
        j += i

ans = 0
for x in range(3, 10**7+1):
    if sieve[x] == sieve[x-1]:
        ans += 1

print(f'Answer: {ans}')

