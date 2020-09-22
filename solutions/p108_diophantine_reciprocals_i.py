import time
import math
import eulerlib
# ==============================================================================


def numDivisors(n):
    factors = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            factors.append((i, 2*cnt))
        i += 1
    if n > 1:
        factors.append((n, 2))

    ans = 1
    for f in factors:
        ans *= f[1] + 1
    return (ans + 1) // 2


def main(N):
    ans = 0

    MAXV = 2*3*5*7*11*13*17
    for n in range(2, MAXV+1):
        cnt_divs = numDivisors(n)
        if cnt_divs > N:
            ans = n
            break

    return ans


if __name__ == '__main__':
    start_t = time.time()
    ans = main(1000)
    prx_t = time.time() - start_t

    print(f'Answer: {ans} - Processing time: {prx_t:.3f}')
