def isPal(x):
    for i in range(len(x) // 2):
        if x[i] != x[len(x) - i - 1]:
            return False
    return True


def add(x, y):
    ans, c = [], 0
    for i in range(len(x)):
        s = x[i] + y[i] + c
        ans.append(s % 10)
        c = s // 10
    if c > 0:
        ans.append(c)
    return ans


def isLychrel(x):
    cnt = 1
    while cnt < 50:
        y = x[::-1]
        x = add(x, y)
        if isPal(x):
            return False
        cnt += 1
    return True


def toList(x):
    X = []
    while x > 0:
        X.append(x % 10)
        x //= 10
    return X


ans = 0
for x in range(1, 10000):
    X = toList(x)
    if isLychrel(X):
        ans += 1

print(f'Answer: {ans}')
