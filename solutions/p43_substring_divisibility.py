from itertools import permutations
import time

divs = [2, 3, 5, 7, 11, 13, 17]

def isOK(p):
    if p[3] % 2 == 1 or p[5] != 5: return False

    for i in range(1, 8):
        x = p[i] * 100 + p[i+1] * 10 + p[i+2]
        if x % divs[i-1] != 0:
            return False
    return True

start_t = time.time()
ans = 0
for perm in list(permutations(list(range(10)))):
    if perm[0] == 0:
        continue
    n = 0
    for d in perm: 
        n = n*10 + d

    if isOK(perm):
        ans += n
prx_t = time.time() - start_t

print(f'Answer: {ans}')

print(f'Procesed time: {prx_t:.4f}')
