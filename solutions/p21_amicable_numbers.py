def d(x):
    ans = 0
    i = 2
    while i*i <= x:
        if x % i == 0:
            ans += i
            if i*i != x:
                ans += x // i
        i += 1
    return ans + 1


prx = set()
ans = 0

for i in range(1, 10000):
    j = d(i)
    print(i, j)
    if i == j or j in prx: continue

    if d(j) == i:
        print(i, j)
        ans += i + j
        prx.add(i)
        prx.add(j)

print(ans)

