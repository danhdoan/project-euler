import time
import eulerlib


def main(N):
    start_t = time.time()
    primes = eulerlib.generatePrimes(N // 2 + 1)
    prx_t = time.time() - start_t
    print(f'Primes generated: {prx_t:.3f}')

    ans = 0
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            p = primes[i] * primes[j]
            if p >= N:
                break
            ans += 1
    return ans


if __name__ == '__main__':
    start_t = time.time()
    ans = main(10**8)
    prx_t = time.time() - start_t

    print(f'Answer: {ans} - Processing time: {prx_t:.3f}')
