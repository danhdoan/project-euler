def add(a, b):
    while len(a) < len(b):
        a.append(0)

    ans = []
    c = 0
    for i in range(len(a)):
        s = a[i] + b[i] + c
        ans.append(s % 10)
        c = s // 10
    if c > 0:
        ans.append(c)
    return ans


f0 = [0]
f1 = [1]

i = 1
while True:
    i += 1
    f2 = add(f0, f1)

    if len(f2) == 1000:
        print(i)
        break

    f0 = f1
    f1 = f2
