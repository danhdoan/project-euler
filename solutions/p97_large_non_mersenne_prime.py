#28433×27830457+1.


def pow(a, b, MOD):
    if b == 0:
        return 1

    p = pow(a, b//2, MOD)
    p = p * p % MOD
    if b & 1:
        p = p * a % MOD 

    return p

a, b = 2, 7830457
MOD = 10**10

ans = (28433 * pow(a, b, MOD) % MOD + 1) % MOD
print(f'Answer: {ans}')
