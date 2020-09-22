import time


def sumDigit(x):
    ans = 0
    while x > 0:
        ans += x % 10
        x //= 10
    return ans


def main(N):
    MAXV = 10**15
    powers = set() 
    for x in range(2, 100):
        p = 1
        while p*x <= MAXV:
            p *= x
            s = sumDigit(p)
            if s == 1: continue
            if s == x and p >= 10:
                powers.add(p)

    powers = sorted(list(powers))
    ans = powers[N - 1]
    return ans

if __name__ == '__main__':
    start_t = time.time()
    ans = main(30)
    prx_t = time.time() - start_t

    print(f'Answer: {ans} - Processing time: {prx_t:.3f}')
