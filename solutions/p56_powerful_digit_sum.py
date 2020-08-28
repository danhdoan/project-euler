def mul_single(a, b):
    ans = []
    c = 0

    for i in range(len(a)):
        p = b * a[i] + c 
        ans.append(p % 10)
        c = p // 10

    if c > 0:
        ans.append(c)
    return ans


def add(a, b):
    mx_len = max(len(a), len(b))
    if len(a) < mx_len:
        while len(a) < mx_len:
            a.append(0)
    else:
        while len(b) < mx_len:
            b.append(0)

    c = 0
    ans = []
    for i in range(mx_len):
        s = c + a[i] + b[i]
        ans.append(s % 10)
        c = s // 10

    if c > 0:
        ans.append(c)
    return ans


def mul(a, b):
    ans = [0]

    cnt = 0
    while b > 0:
        prod = [0] * cnt + mul_single(a, b % 10)
        cnt += 1
        b //= 10

        ans = add(ans, prod)
    return ans


def sum_power(a, b):
    ans = [1]
    
    for i in range(b):
        ans = mul(ans, a)

    return sum(ans)


ans = 0
for a in range(2, 100):
    for b in range(100):
        ans = max(ans, sum_power(a, b))
print(f'Answer: {ans}')
