import bisect

P = [n*(3*n - 1) // 2 for n in range(1, 2401)]

ans = float('inf')
for y in range(len(P)):
    for x in range(y+2, len(P)):
        s = P[x] + P[y]
        if s % 2 == 1: continue

        Pk = s // 2
        idx = bisect.bisect(P, Pk) - 1
        if P[idx] != Pk: continue

        Pj = P[x] - Pk
        idx = bisect.bisect(P, Pj) - 1
        if P[idx] != Pj: continue

        if ans > P[y]:
            ans = min(ans, P[y])
            break
    else:
        continue
    break

print(f'Answer: {ans}')
