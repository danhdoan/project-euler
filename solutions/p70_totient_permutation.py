import time

start_t = time.time()
N = 10**7

sieve = [True] * N
phi = [i for i in range(N)]

for i in range(2, N//2 + 1):
    if not sieve[i]: continue
    for j in range(2*i, N, i):
        sieve[j] = False
        phi[j] -= phi[j] // i

for i in range(2, N):
    if sieve[i]:
        phi[i] -= phi[i] // i

ans = -1
mn_ratio = float('inf')
error = 0
for n in range(2, N):
    ratio = n / phi[n]
    if ratio < mn_ratio:
        if sorted(str(n)) == sorted(str(phi[n])):
            mn_ratio = ratio
            ans = n

prx_t = time.time() - start_t
print(f'Answer: {ans} - Time processed: {prx_t:.3f}')
