import math

def check(a, b, x, y):
    if b == 0 or y == 0: return False
    return a*y == b*x

s = set() 
for x in range(10, 100):
    for y in range(x+1, 100):
        a, b = x // 10, x % 10
        c, d = y // 10, y % 10

        if check(x, y, a, d) and b == c:
            print('check:', x, y)
            s.add((x, y))
        if check(x, y, b, c) and a == d:
            print('check:', x, y)
            s.add((x, y))
        if check(x, y, b, d) and a == c:
            print('check:', x, y)
            s.add((x, y))

num = den = 1
for p in s: 
    num *= p[0]
    den *= p[1]

ans = den // math.gcd(num, den)
print(f'Answer: {ans}')
