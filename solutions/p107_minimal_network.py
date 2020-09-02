class UnionFind:
    def __init__(self, N):
        self.ids = [-1] * N

    def root(self, u):
        if self.ids[u] < 0:
            return u
        self.ids[u] = self.root(self.ids[u])
        return self.ids[u]

    def union(self, u, v):
        if self.ids[u] > self.ids[v]:
            u, v = v, u

        self.ids[u] += self.ids[v]
        self.ids[v] = u


N = 40
edges = []

with open('p107_network.txt', 'r') as f:
    data = f.read().strip().split('\n')
    for i, line in enumerate(data):
        line = line.split(',')
        for j, w in enumerate(line):
            if j >= i or w == '-': continue
            edges.append((i, j, int(w)))

edges = sorted(edges, key=lambda e: e[-1])
total_weight = sum([e[-1] for e in edges])
reduced_weight = 0

uf = UnionFind(N)
for (u, v, w) in edges:
    u = uf.root(u)
    v = uf.root(v)

    if u != v:
        reduced_weight += w
        uf.union(u, v)

print(f'Answer: {total_weight - reduced_weight}')
