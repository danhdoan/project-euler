def add(x, y):
    c = 0
    ans = []
    for i in range(max(len(x), len(y))):
        s = c
        if i < len(x): s += x[i]
        if i < len(y): s += y[i]

        ans.append(s % 10)
        c = s // 10 
    if c > 0:
        ans.append(c)

    return ans


f1 = [1]
f2 = [1]

k = 3
while True:
    f = add(f1, f2)

    if len(f) >= 9:
        if 0 not in f[:9] and len(set(f[:9])) == 9 \
                and 0 not in f[-9:] and len(set(f[-9:])) == 9:
            break

    f1 = f2
    f2 = f
    k += 1
    if k % 1000 == 0:
        print('debug', k, len(f2))

print(f'Anser: {k}')

