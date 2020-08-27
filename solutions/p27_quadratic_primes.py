def is_prime(x):
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return x > 1


def process(a, b):
    n = 0
    while True:
        x = n*n + n*a + b
        if x <= 1 or not is_prime(x):
            break
        n += 1
    return n


ans, max_len = -1, 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        length = process(a, b)

        if max_len < length:
            max_len = length
            ans = a*b
            print(a, b, length)

print("Answer:", ans)
