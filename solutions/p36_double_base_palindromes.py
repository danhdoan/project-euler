ans = 0

for x in range(1, 1000001):
    x_b = bin(x)[2:]
    x_s = str(x)

    if x_s == x_s[::-1] and x_b == x_b[::-1]:
        ans += x

print(f'Answer: {ans}')

