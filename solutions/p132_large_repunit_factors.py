import time

def genPrimes(N = 10**6):
    sieve = [True] * N

    for i in range(2, N//2+1):
        if not sieve[i]: continue
        for j in range(2*i, N, i):
            sieve[j] = False

    primes = []
    for i in range(2, N):
        if sieve[i]:
            primes.append(i)
    return primes


def modPow(a, b, MOD):
    if b == 0:
        return 1

    pw = modPow(a, b//2, MOD)
    pw = pw * pw % MOD
    if b & 1:
        pw = pw * a % MOD
    return pw


def isOK(k, p):
    return modPow(10, k, 9*p) == 1


def main(K):
    primes = genPrimes()
    cnt = 0
    ans = 0
    for p in primes:
        if isOK(K, p):
            cnt += 1
            ans += p
            #print('debug:', cnt, p)
            if cnt == 40:
                break

    return ans


if __name__ == '__main__':
    K = 10**9

    start_t = time.time()
    ans = main(K)
    prx_t = time.time() - start_t

    print(f'Answer: {ans} - Processing time: {prx_t:.3f}')

