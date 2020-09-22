import math

def is_less(u, v):
    return u[0] * v[1] < u[1] * v[0]


N = 12000
lower = (1, 3)
upper = (1, 2)

ans = 0
st = [(0, 1, 1, 1)]
while len(st):
    a, b, c, d = st.pop()
    x, y = a+c, b+d
    g = math.gcd(x, y)
    x //= g
    y //= g

    if not (x <= N and y <= N):
        continue
    ans += 1 if is_less(lower, (x, y)) and is_less((x, y), upper) else 0

    st.append((a, b, x, y))
    st.append(( x, y, c, d))


print(f'Answer: {ans}')
