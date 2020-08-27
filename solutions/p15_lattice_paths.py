a = [[0]*22 for _ in range(22)]

a[0][1] = 1
for i in range(1, 22):
    for j in range(1, 22):
        a[i][j] = a[i-1][j] + a[i][j-1]

print(a[-1][-1])
