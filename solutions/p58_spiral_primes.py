def isPrime(x):
    i = 2
    while i*i <= x:
        if x % i == 0: return False
        i += 1
    return x > 1


N = 50001
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

ans = -1

prime_cnt = 0
for n in range(3, N, 2):
    dir = 0
    cx = N // 2 + n // 2
    cy = N // 2 + n // 2

    v = n*n
    for _ in range(4):
        for __ in range(n - 1):
            if (cx == cy or cx + cy == N-1) and isPrime(v):
                prime_cnt += 1
            cx += dx[dir]
            cy += dy[dir]
            v -= 1
        dir = (dir + 1) % 4

    if prime_cnt * 10 < 2*n - 1:
        ans = n
        break

    if n % 999 == 0:
        print('debug', n)
        print(prime_cnt, 2*n-1)

print(f'Answer: {ans}')
