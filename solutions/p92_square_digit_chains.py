ans = 0
for x in range(2, 10**7):
    while x != 1 and x != 89:
        y = 0
        while x > 0:
            y += (x % 10)**2
            x //= 10
        x = y

    if x == 89:
        ans += 1

print(f'Answer: {ans}')
