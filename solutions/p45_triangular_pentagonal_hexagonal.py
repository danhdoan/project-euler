import math

for n in range(1, 100000):
    H = n*(2*n - 1)

    # verify pentagonal
    p = int((1 + math.sqrt(1 + 24*H)) / 6)
    if p*(3*p - 1) // 2 != H:
        continue

    # verify triangle
    t = int((-1 + math.sqrt(1 + 8*H)) / 2)
    if t*(t + 1) // 2 == H:
        print(t, p, n, H)
