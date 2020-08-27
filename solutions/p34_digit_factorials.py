f = [1, 1]
for i in range(2, 10):
    f.append(i * f[-1])
print(f)

def ok(i):
    x = i
    s = 0
    while i > 0:
        s += f[i % 10]
        i //= 10
    return s == x


ans = 0
for i in range(3, 2540161):
    if ok(i):
        ans += i
        print(i)

print(ans)
