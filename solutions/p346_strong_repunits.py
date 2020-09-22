import time
import math


def main(N):
    hist = set()
    for b in range(2, 1000001):
        n = 3
        while True:
            x = (b**n - 1) // (b - 1)
            if x < N:
                hist.add(x)
            else: break
            n += 1

    ans = sum(hist)

    return ans + 1

if __name__ == '__main__':
    start_t = time.time()
    ans = main(10**12)
    prx_t = time.time() - start_t

    print(f'Answer: {ans} - Processing time: {prx_t:.3f}')
