import time
import math

def tryConvert(w, x):
    """Try to convert a word to an integer"""

    d = {}
    hist = set()
    for i in range(len(w) - 1, -1, -1):
        last = x % 10
        if w[i] in d:
            if d[w[i]] != last:
                return False, None
        else:
            if last in hist:
                return False, None
            else:
                d[w[i]] = last
                hist.add(last)
        x //= 10
    return True, d


def convert(w, d):
    """Try convert a word to an integer based on a given rule"""

    ans = 0
    for i, c in enumerate(w):
        ans = ans * 10 + d[c]
    if len(str(ans)) != len(w):
        return False, None
    return True, ans


def main(file_path):
    #extract raw data
    with open(file_path, 'r') as f:
        data = list(map(lambda x: x[1:-1], f.read().strip().split(',')))

    # find all anagrams
    d = {}
    for w in data:
        w_s = ''.join(sorted(w))
        d.setdefault(w_s, []).append(w)

    # find maximum length of words
    # to find maximum value of integers to be squared
    mx_len = 0
    for k, v in d.items():
        if len(v) == 1: continue
        mx_len = max(mx_len, len(v[0]))

    MAXN = int(math.sqrt(10**mx_len - 1))

    # pre-compute squared numbers 
    # and store by length for later indexing
    sqrs_d = {}
    for i in range(4, MAXN + 1):
        sqr = i*i
        l = len(str(sqr))
        sqrs_d.setdefault(l, []).append(sqr)

    # main process
    ans = 0
    for k, v in d.items():
        if len(v) == 1: continue

        for i, w1 in enumerate(v):
            l = len(w1)
            for sqr in sqrs_d[l]:
                flag, d = tryConvert(w1, sqr)
                if not flag: continue

                for j, w2 in enumerate(v[i+1:]):
                    ok, x = convert(w2, d)
                    if not ok: continue
                    sqrt_x = int(math.sqrt(x))
                    if sqrt_x**2 == x:
                        ans = max(ans, max(sqr, x))
    return ans


if __name__ == '__main__':
    start_t = time.time()
    ans = main('p098_words.txt')
    prx_t = time.time() - start_t
    print(f'Answer: {ans} - Processing time: {prx_t:.3f}')
