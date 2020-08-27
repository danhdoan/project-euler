def isRed(x):
    sm = 0
    i = 2
    while i*i <= x:
        if x % i == 0:
            sm += i
            if i*i != x:
                sm += x // i
        i += 1
    return sm + 1 > x


MAXN = 28123

reds = []
for i in range(1, MAXN+1):
    if isRed(i):
        reds.append(i)

combined = [False] * (MAXN+1)
for i, x in enumerate(reds):
    for j in range(i, len(reds)):
        if x + reds[j] <= MAXN:
            combined[x + reds[j]] = True

ans = 0
for i, ok in enumerate(combined):
    if not ok:
        ans += i
print(ans)
