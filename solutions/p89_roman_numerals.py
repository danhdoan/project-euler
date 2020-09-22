import time

def substitute(roman, d):
    for u, v in d:
        roman = roman.replace(u, v)
    return roman


def main(file_path):
    with open(file_path, 'r') as f:
        data = f.read().strip().split('\n')

    d = [
        ('VIIII', 'IX'), ('IIII', 'IV'), 
        ('LXXXX', 'XC'), ('XXXX', 'XL'), 
        ('DCCCC', 'CM'), ('CCCC', 'CD')]

    ans = 0
    for roman in data:
        s_roman = substitute(roman, d)
        ans += len(roman) - len(s_roman)
    return ans


if __name__ == '__main__':
    start_t = time.time()
    ans = main('p089_roman.txt')
    prx_t = time.time() - start_t

    print(f'Answer: {ans} - Processing time: {prx_t:.3f}')
