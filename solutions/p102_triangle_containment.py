def doubleArea(xa, ya, xb, yb, xc, yc):
    return abs((xb-xa)*(yc-ya) - (xc-xa)*(yb-ya))

def isInside(xa, ya, xb, yb, xc, yc):
    sa = doubleArea(0, 0, xa, ya, xb, yb)
    sb = doubleArea(0, 0, xb, yb, xc, yc)
    sc = doubleArea(0, 0, xc, yc, xa, ya)
    s = doubleArea(xa, ya, xb, yb, xc, yc)
    return sa + sb + sc == s

ans = 0
with open('p102_triangles.txt', 'r') as f:
    points = list(map(lambda s: list(map(int, s.split(','))), \
            f.read().strip().split('\n')))

    for p in points:
        ans += 1 if isInside(*p) else 0

print(f'Answer: {ans}')

