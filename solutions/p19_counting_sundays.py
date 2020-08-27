DAYS = [-1, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

day_cnt = 0

ans = 0
for y in range(1901, 2001):
    for m in range(1, 13): 
        day_cnt += DAYS[m]
        if m == 3 and (y % 4 == 0 and y % 100 != 0 or y % 400 == 0):
            day_cnt += 1

        print(y, m, day_cnt % 7)
        if day_cnt % 7 == 1:
            ans += 1

print(ans)
