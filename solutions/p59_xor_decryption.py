#101 120 112
def process(data, code):
    ans = []
    for i in range(0, len(data), 3):
        x = code[0] ^ data[i]
        ans.append(chr(x))

        x = code[1] ^ data[i+1]
        ans.append(chr(x))

        x = code[2] ^ data[i+2]
        ans.append(chr(x))

    return True, ''.join(ans)


with open('p059_cipher.txt', 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

#writer = open('output.txt', 'w')
#for a in range(ord('a'), ord('z')+1):
#    for b in range(ord('a'), ord('z')+1):
#        for c in range(ord('a'), ord('z')+1):
#            flag, txt = process(data, [a, b, c])
#            if not flag: continue
#            writer.write(f'{a} {b} {c} ' + ''.join(txt[:20]) + '\n')
#writer.close()
flag, txt = process(data, [101, 120, 112])
ans = sum(ord(c) for c in txt)
print(f'Answer: {ans}')

