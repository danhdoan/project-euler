def process(x):
    n = 1
    curr = ''
    while True:
        y = str(x * n)
        if '0' in y:
            return -1

        curr += y
        if len(curr) != len(set(curr)):
            return -1

        if len(curr) == 9:
            break
        n += 1

    return int(curr)


ans = 0
for x in range(1000001):
    res = process(x)
    if res != -1:
        print(res)
        ans = max(ans, process(x))

print(f'Answer: {ans}')
