import math

def isLess(u, v):
    return u[0] * v[1] < u[1] * v[0]


def findMid(u, v):
    num = u[0] + v[0]
    den = u[1] + v[1]
    g = math.gcd(num, den)
    return num // g, den // g


n = 1000000
lo = (1, n)
hi = (n-1, n)
target = (3, 7)

ans = None
while True:
    mid = findMid(lo, hi)
    if mid[0] >= n or mid[1] > n:
        break
    if isLess(mid, target):
        ans = mid
        lo = mid
        hi = target
    else:
        hi = mid

print(f'Answer: {ans[0]}')
