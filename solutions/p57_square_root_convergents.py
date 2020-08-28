def func(a, b):
    a += 2*b
    return b, a

ans, turn = 0, 2
a, b = 1, 2

while turn <= 1000:
    a, b = func(a, b)
    num = a + b
    den = b

    turn += 1

    if len(str(num)) > len(str(den)):
        ans += 1

print(f'Answer: {ans}')
