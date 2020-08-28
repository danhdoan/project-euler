x = 100
while True:
    x_s = str(x)
    if x_s[0] != '1' or x_s[1] > '6': 
        x += 1
        continue
    x_s = sorted(x_s)

    ok = True
    for i in range(2, 7):
        y = str(x*i)
        if sorted(y) != x_s:
            ok = False
            break

    if ok:
        print(x)
        break

    x += 1

