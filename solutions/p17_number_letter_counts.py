letters = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4}
tens = {2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
dums = {10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}


def process(x):
    if x < 10:
        return letters[x]
    if x < 20:
        return dums[x]
    return tens[x // 10] + (letters[x % 10] if x % 10 > 0 else 0)


# one thousand: 11
ans = 11
for i in range(1, 1000):
    if i < 100:
        ans += process(i)
    else:
        #hundred : 7
        ans += letters[i // 100] + 7
        if i % 100 > 0:
            ans += 3 + process(i % 100) # and: 3

print(f'Answer: {ans}')
