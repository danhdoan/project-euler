import time

start_t = time.time()
N = 10**6 + 1
phi = [i - 1 for i in range(N)]
for i in range(2, N):
    for j in range(2*i, N, i):
        phi[j] -= phi[i]

max_num, max_den = 0, 1
ans = -1

for n in range(2, N):
    num = n
    den = phi[n]
    if num * max_den > max_num * den:
        ans = n
        max_num, max_den = num, den
prx_t = time.time() - start_t
print(f'Answer: {ans} - Processing time: {prx_t:.3f}')
