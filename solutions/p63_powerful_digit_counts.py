ans = 1

for x in range(2, 10):
    p = 1
    for i in range(1, 40):
        p *= x
        l = len(str(p))
        if l == i:
            print(x, i, p)
            ans += 1
        elif l > i:
            break

print(f'Answer: {ans}')

