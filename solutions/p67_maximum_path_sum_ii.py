with open('p067_triangle.txt') as f:
    data = list(map(lambda s: list(map(int, s.split())), \
            f.read().strip().split('\n')))

curr = data[0]
print(curr)
for i in range(1, len(data)):
    tmp = []
    for j in range(len(data[i])):
        left = curr[j-1] if j > 0 else 0
        right = curr[j] if j < len(curr) else 0

        tmp.append(data[i][j] + max(left, right))

    curr = tmp

print(f'Answer: {max(curr)}')
