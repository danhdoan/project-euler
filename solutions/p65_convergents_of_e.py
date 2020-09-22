import time
import math


def main(n):
    terms = [2, 1]
    for t in range(2, 67, 2):
        terms.extend([t, 1, 1])
    
    num, den = terms[n-1], 1
    for i in range(n-2, -1, -1):
        num, den = terms[i]*num + den, num

    ans = 0
    while num > 0:
        ans += num % 10
        num //= 10

    return ans


if __name__ == '__main__':
    start_t = time.time()
    ans = main(100)
    prx_t = time.time() - start_t

    print(f'Answer: {ans} - Processing time: {prx_t:.3f}')
