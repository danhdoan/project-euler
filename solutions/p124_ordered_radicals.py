def calc(x):
    ans = 1
    i = 2
    while i*i <= x:
        if x % i == 0:
            ans *= i
            while x % i == 0:
                x //= i
        i += 1
    if x > 1: ans *= x
    return ans


N = 10**5
prime = [True] * (N+1)
rad = [1] * (N+1)

for i in range(2, N//2 + 1):
    if not prime[i]: continue
    for j in range(2*i, N+1, i):
        prime[j] = False
        rad[j] *= i
for i in range(N+1):
    if prime[i]:
        rad[i] *= i

E = sorted([(n, rad[n]) for n in range(1, len(rad))], key=lambda x:x[1])
print(f'Answer: {E[9999][0]}')

