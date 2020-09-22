import time

start_t = time.time()
N = 10**4
hist = {}
for i in range(N+1):
    c = ''.join(sorted(str(i**3)))
    hist.setdefault(c, []).append(i)

ans = float('inf')
for k, v in hist.items():
    if len(v) == 5:
        ans = min(ans, min(v))

prx_t = time.time() - start_t
print(f'Answer: {ans**3} - Processing time: {prx_t:.3f}')
