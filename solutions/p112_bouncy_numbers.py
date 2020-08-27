def inc(x):
    prv = 10
    while x > 0:
        y = x % 10
        if y > prv:
            return False
        prv = y
        x //= 10
    return True

def dec(x):
    prv = -1
    while x > 0:
        y = x % 10
        if y < prv:
            return False
        prv = y
        x //= 10
    return True


i = 1
cnt = 0
while True:
    if not (inc(i) or dec(i)):
        cnt += 1
    if cnt * 100 / i >= 99:
        print(i)
        break
    i += 1
