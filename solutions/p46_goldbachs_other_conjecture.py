def is_prime(x):
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return x > 1


def check(x):
    i = 0
    while i*i*2 < x:
        p = x - 2*i*i
        if is_prime(p):
            return True

        i += 1
    return False


x = 35
ans = -1
while True:
    found = check(x)
    if not found:
        ans = x
        break
    x += 2

print(f'Answer: {ans}')
