ans = 0

def comb(n, k):
    res = 1
    for i in range(k):
        res = res * (n - i) // (i + 1)

    return res

for n in range(1, 101):
    less = 0
    for k in range(n+1):
        c = comb(n, k)
        if c <= 1000000:
            less += 1
        else:
            break
    else:
        continue

    ans += n+1 - less*2
    if n % 2 == 0 and less == n // 2:
        ans -= 1


print(f'Answer: {ans}')
