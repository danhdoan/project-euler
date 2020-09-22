import time
import math
import eulerlib
# ==============================================================================


def main(N):
    MAXP = int(math.sqrt(N)) + 1
    primes = eulerlib.generatePrimes(MAXP)
    print(f'Num. Primes: {len(primes)}')

    hist = set()
    for i, p1 in enumerate(primes):
        a = p1**2
        for j, p2 in enumerate(primes):
            b = p2**3
            if a + b >= N: break
            for k, p3 in enumerate(primes):
                c = p3**4
                sm = a + b + c
                if sm >= N: break
                hist.add(sm)
    ans = len(hist)
    return ans

if __name__ == '__main__':
    start_t = time.time()
    ans = main(50*10**6)
    prx_t = time.time() - start_t

    print(f'Answer: {ans} - Processing time: {prx_t:.3f}')
