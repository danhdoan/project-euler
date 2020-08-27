def isOK(a):
    s = []
    for x in a:
        while x > 0:
            s.append(x % 10)
            x //= 10

    return len(s) == len(set(s)) and not 0 in s and len(set(s)) == 9


def process():
    ans = set()
    for a in range(2, 100):
        for b in range(123, 10000):
            c = a * b
            if isOK([a, b, c]):
                print(a, b, c)
                ans.add(c)
    return ans

ans = sum(process())
print("Answer:", ans)
