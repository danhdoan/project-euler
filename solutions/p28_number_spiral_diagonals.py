N = 1001
p = [[0]*N for _ in range(N)]

x, y = 0, N-1
dx, dy = 0, -1
for i in range(N*N, 0, -1):
    p[x][y] = i

    if 0 <= x+dx < N and 0 <= y+dy < N and p[x+dx][y+dy] == 0:
        x += dx
        y += dy
    else:
        if dx == 0 and dy == -1: dx, dy = 1, 0
        elif dx == 1 and dy == 0: dx, dy = 0, 1
        elif dx == 0 and dy == 1: dx, dy = -1, 0
        else: dx, dy = 0, -1

        x += dx
        y += dy

ans = 0
for i in range(N):
    ans += p[i][i]
    if i != N // 2: ans += p[i][N - 1 - i]

print(f'Answer: {ans}')
