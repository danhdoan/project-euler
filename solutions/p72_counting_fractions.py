import eulerlib

N = 1000000
ans = 0
for i in range(2, N+1):
    ans += eulerlib.totient(i)

print(f'Answer: {ans}')
