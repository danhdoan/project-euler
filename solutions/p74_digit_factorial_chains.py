import time

start_t = time.time()
ft = [1]
for i in range(1, 10):
    ft.append(ft[-1] * i)

def conv(n):
    ans = 0
    while n > 0:
        ans += ft[n % 10]
        n //= 10
    return ans

memory = {}
N = 10**6
ans = 0
for n in range(N+1):
    hist = set()
    while n not in hist:
        hist.add(n)

        if n in memory:
            n = memory[n]
        else:
            next = conv(n)
            memory[n] = next
            n = next
    if len(hist) == 60:
        ans += 1
prx_t = time.time() - start_t

print(f'Answer: {ans}')
print(f'Time processed: {prx_t:.3f}')
        
