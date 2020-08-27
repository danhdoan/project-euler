with open('p022_names.txt', 'r') as f:
    data = sorted(list(map(lambda x: x[1:-1], f.read().strip().split(','))))

ans = 0
for i, name in enumerate(data):
    score = sum(list(map(lambda x: ord(x) - ord('A') + 1, list(name))))
    ans += score * (i + 1)

print(ans)
