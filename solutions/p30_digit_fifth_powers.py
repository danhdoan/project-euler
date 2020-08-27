d = {i: i**5 for i in range(10)}

def ok(x):
    X = x
    ans = 0
    while x > 0:
        ans += d[x % 10]
        x //= 10
    return ans == X


ans = 0
for i in range(2, 6 * d[9]):
    if ok(i):
        print(i)
        ans += i

print("Answer:", ans)
