N = 10**8 + 2
primes = [True] * N
for i in range(2, N//2):
    if not primes[i]: continue
    j = 2*i
    while j < N:
        primes[j] = False
        j += i

def ok(x):
    i = 1
    while i*i <= x:
        if x % i == 0:
            s = i + x // i
            if not primes[s]:
                return False
        i += 1
    return True


ans = 1

for x in range(2, N, 2):
    if ok(x):
        ans += x

print(f'Answer: {ans}')

