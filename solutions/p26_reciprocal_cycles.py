def ok(x):
    while x % 2 == 0: x //= 2
    while x % 5 == 0: x //= 5
    return x == 1


def getLength(d):
    history = {}
    a = 1
    idx = 1
    while True:
        a = a % d * 10
        if a in history:
            return idx - history[a]
        history[a] = idx
        idx += 1


ans, max_len = 0, 0
for d in range(2, 1000):
    if ok(d): continue
    l = getLength(d)

    if max_len < l:
        ans, max_len = d, l

print(f'Answer: {ans}')

# get remainder and multiply by 10
# 1   7  0
# 10  7  1
# 30  7  4
# 20  7  2
# 60  7  8
# 40  7  5
# 50  7  7
# 10  -> repeated
