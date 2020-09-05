import math
import time

start_t = time.time()
ans = -1
for i in range(10**9, int(math.sqrt(1929394959697989990)), 10):
    x = i // 10
    if x % 10 != 3 and x % 10 != 7: continue
    p = str(i**2)
    for j in range(0, len(p)-1, 2):
        if j//2+1 != int(p[j]): 
            ok = False
            break
    else:
        ans = i
        break
prx_t = time.time() - start_t

print(f'Answer: {ans} - Processing time: {prx_t:.3f}')
