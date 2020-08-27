MAXN = 1000001
sieve = [True] * MAXN

for i in range(2, MAXN//2):
    j = 2*i
    while j < MAXN:
        sieve[j] = False
        j += i


def isOK(x):
    if x == 2 or x == 3 or x == 5: return True
    s = list(map(int, str(x)))
    for d in s:
        if d in [2, 4, 6, 8, 0, 5]:
            return False

    if sum(s) % 3 == 0 or sum(s) % 9 == 0:
        return False

    for i in range(len(s)):
        y = x % 10
        x = y * 10**(len(s)-1) + x // 10
        if not sieve[x]:
            return False
    return True


ans = 0
for i in range(2, MAXN):
    if isOK(i):
        print(i)
        ans += 1

print(ans)
