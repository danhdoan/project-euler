import math


words = None
with open('p042_words.txt', 'r') as f:
    words = list(map(lambda x: x[1:-1], f.read().strip().split(',')))

ans = 0
for word in words:
    code = 0
    for c in word:
        code += ord(c) - ord('A') + 1

    n = int(math.sqrt(2*code))
    if n*(n+1) == 2*code:
        ans += 1

print(f'Answer: {ans}')
