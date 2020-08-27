curr = [1]

for i in range(1000):
    next = []

    c = 0
    for j in range(len(curr)):
        p = 2 * curr[j] + c
        next.append(p % 10)
        c = p // 10

    if c != 0:
        next.append(c)

    curr = next

print(sum(curr))
