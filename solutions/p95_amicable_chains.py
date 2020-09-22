import time

N = 10**6
sieve = [1] * (N + 1)
sieve[0] = sieve[1] = 0

start_t = time.time()
for i in range(2, N//2 + 1):
    for j in range(2*i, N+1, i):
        sieve[j] += i
prx_t = time.time() - start_t
print(f'Sieve generated: {prx_t}')

ans, mx_len = -1, 0
for n in range(N+1):
    mn_ele = x = n
    cnt = 0
    hist = set([x])
    found = False
    while x <= N:
        cnt += 1
        x = sieve[x]
        if x == n:
            found = True
            break
        if x in hist: break
        hist.add(x)
        mn_ele = min(mn_ele, x)

    if found and mx_len < cnt:
        mx_len = cnt
        ans = mn_ele

print(f'Answer: {ans} - Max. Length: {mx_len}')
