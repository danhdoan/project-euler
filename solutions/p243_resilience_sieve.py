N = 260_000_000 + 1
phi = [i-1 for i in range(N)]
print('init done')

for i in range(2, N):
    for j in range(2*i, N, i):
        phi[j] -= phi[i]
    if i % 1000000 == 0:
        print('debug', i)


t_num, t_den = 15499, 94744
#t_num, t_den = 4, 10

for x in range(2, N):
    num, den = phi[x], x - 1
    if num * t_den < den * t_num:
        break

    if x % 100000 == 0: 
        print('debug', x)
    
print(f'Answer: {x}')
