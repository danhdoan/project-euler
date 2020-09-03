def phi(x):
    ans = x
    i = 2
    while i*i <= x:
        if x % i == 0:
            ans -= ans // i
            while x % i == 0:
                x //= i
        i += 1
    if x > 1:
        ans -= ans // x
    return ans


def isPrime(x):
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return x > 1


t_num, t_den = 15499, 94744
num = den = 1
prime = 2
while True:
    num *= prime - 1
    den *= prime

    while True:
        prime += 1
        if isPrime(prime): break

    if num * t_den < den * t_num:
        for i in range(1, prime):
            n = den * i
            if phi(n) * t_den < (n - 1) * t_num:
                print(n)
                break
        else:
            continue
        break
