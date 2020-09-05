from collections import deque

def bfs(u, target, E, N):
    dist = [float('inf')] * (N**2 + 1)
    dist[u] = 0

    q = deque([u])
    while len(q) > 0:
        u = q.popleft()
        if u not in E: continue
        for (v, w) in E[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                q.append(v)

    return dist[target]


with open('p082_matrix.txt', 'r') as f:
    data = list(map(lambda s: list(map(int, s.split(','))), f.read().strip().split('\n')))
#data = [
#        [131, 673, 234, 103, 18],
#        [201, 96, 342, 965, 150],
#        [630, 830, 746, 422, 111],
#        [537, 699, 497, 121, 956],
#        [805, 732, 524, 37, 331]]

N = len(data)
E = {}
for i in range(N):
    E.setdefault(0, []).append((i*N+1, data[i][0]))

for i in range(N):
    for j in range(N-1):
        v1 = i*N + j + 1

        if i > 0:
            v2 = (i-1)*N + j + 1
            E.setdefault(v1, []).append((v2, data[i-1][j]))
        if i + 1 < N:
            v2 = (i+1)*N + j + 1
            E.setdefault(v1, []).append((v2, data[i+1][j]))
            
        v2 = i*N + j + 2
        E.setdefault(v1, []).append((v2, data[i][j+1]))

ans = float('inf') 
for i in range(N):
    v = (i+1)*N 

    dist = bfs(0, v, E, N)
    ans = min(ans, dist)

print(f'Answer: {ans}')
