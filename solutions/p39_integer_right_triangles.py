import math


def check(p):
    c_lower, c_upper = int(p / math.sqrt(8)), p // 2

    ans = 0
    for c in range(c_lower, c_upper):
        B = p - c
        C = p * p // 2 - p*c

        delta = B*B - 4*C
        if delta < 0:
            continue

        b1 = (B + int(math.sqrt(delta))) // 2
        b2 = (B - int(math.sqrt(delta))) // 2

        a1 = p - b1 - c
        #print('\t', a1, b1, c)
        if 0 < a1 < b1 and a1*a1 + b1*b1 == c*c and \
                a1 + b1 > c and a1 + c > b1 and b1 + c > a1:
            print('\t', a1, b1, c)
            ans += 1

        a2 = p - b2 - c
        #print('\t', a2, b2, c)
        if 0 < a2 < b2 and a2*a2 + b2*b2 == c*c and \
                a2 + b2 > c and a2 + c > b2 and b2 + c > a2:
            print('\t', a2, b2, c)
            ans += 1

    return ans


ans, max_sols = 0, 0
for p in range(4, 1001, 2):
    print('checking:', p)
    sols = check(p)
    if max_sols < check(p):
        ans = p
        max_sols = sols

print(f'Answer: {ans}')
