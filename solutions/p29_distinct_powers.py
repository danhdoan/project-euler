d = set()

def factors(x):
    i = 2
    ans = []
    while i * i <= x:
        if x % i == 0:
            cnt = 0
            while x % i == 0:
                cnt += 1
                x //= i

            ans.extend([i, cnt])
        i += 1

    if x > 1:
        ans.extend([x, 1])
    return tuple(ans)


for a in range(2, 101):
    for b in range(2, 101):
        ft = factors(a)
        ft_ = []
        for i in range(0, len(ft), 2):
            ft_.extend([ft[i], ft[i+1] * b])
        d.add(tuple(ft_))

print("Answer:", len(d))
