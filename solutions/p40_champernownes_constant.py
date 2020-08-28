s = '0'

i = 1
while len(s) < 10000001:
    s += str(i)
    i += 1

ans = 1
i = 1
while i <= 1000000:
    ans *= ord(s[i]) - ord('0')
    i *= 10

print(f'Answer: {ans}')
