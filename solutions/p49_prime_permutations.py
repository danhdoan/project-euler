MAXN = 10000
sieve = [True] * MAXN


for i in range(2, MAXN // 2 + 1):
    j = 2*i
    while j < MAXN:
        sieve[j] = False
        j += i

primes = []
for i in range(1001, 9998):
    if sieve[i]:
        primes.append(i)

for i, p1 in enumerate(primes):
    for j in range(i+1, len(primes)):
        p2 = primes[j]
        diff = p2 - p1
        p3 = p2 + diff
        if p3 < MAXN and sieve[p3]:
            s1, s2, s3 = str(p1), str(p2), str(p3)
            if sorted(s1) == sorted(s2) == sorted(s3):
                print(s1 + s2 + s3)
