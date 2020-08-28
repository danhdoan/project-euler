from itertools import permutations

def is_prime(x):
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return x > 1


ans = 0
for i in range(9, 2, -1):
    L = list(range(1, i+1))
    _perms = list(permutations(L))

    mx = -1
    for _p in _perms:
        x = 0
        for d in _p:
            x = x*10 + d
        
        if is_prime(x):
            mx = max(mx, x)

    if mx != -1:
        ans = mx
        break

print(f'Answer: {ans}')
