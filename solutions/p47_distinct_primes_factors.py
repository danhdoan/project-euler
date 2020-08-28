MAXN = 1000001
nfactors = [0] * MAXN
sieve = [True] * MAXN


for i in range(2, MAXN // 2 + 1):
    j = 2*i
    while j < MAXN:
        sieve[j] = False
        j += i

for i in range(2, MAXN):
    if sieve[i]:
        nfactors[i] += 1
        j = 2*i
        while j < MAXN:
            nfactors[j] += 1
            j += i

for i in range(2, MAXN):
    if i+3 < MAXN:
        if nfactors[i] == nfactors[i+1] == nfactors[i+2] == nfactors[i+3] == 4:
            print(i)
            break
