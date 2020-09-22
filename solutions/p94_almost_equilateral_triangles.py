import time
import math


def tryCalc(x, flag):
    if flag:
        area2 = (3*x-1)*(x-1)**2*(x+1) // 16
    else:
        area2 = (3*x+1)*(x+1)**2*(x-1) // 16

    x = int(math.sqrt(area2))
    return x*x == area2


def main():
    ans = 0

    x = 3
    while True:
        if 3*x - 1 > 10**9: break
        if tryCalc(x, True):
            ans += 3*x - 1

        if 3*x + 1 > 10**9: break
        if tryCalc(x, False):
            ans += 3*x + 1

        #if x % 1000000 == 1: print('debug:', x)
        x += 2
    return ans


if __name__ == '__main__':
    start_t = time.time()
    ans = main()
    prx_t = time.time() - start_t

    print(f'Answer: {ans} - Processing time: {prx_t:.3f}')
