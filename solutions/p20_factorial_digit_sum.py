def prod_line(a, v):
    ans = []
    c = 0
    for d in a:
        p = d * v + c
        ans.append(p % 10)
        c = p // 10
    if c > 0:
        ans.append(c)
    return ans


def prod(a, v):
    nums = []
    cnt = -1
    max_len = 0
    while v > 0:
        d = v % 10
        v //= 10

        cnt += 1
        num = prod_line(a, d)
        for i in range(cnt):
            num = [0] * cnt + num

        max_len = max(max_len, len(num))
        nums.append(num)

    for i in range(len(nums)):
        while len(nums[i]) < max_len:
            nums[i].append(0)

    c = 0
    ans = []
    for j in range(max_len):
        s = c
        for i in range(len(nums)):
            s += nums[i][j]

        ans.append(s % 10)
        c = s // 10

    if c > 0:
        ans.append(c)

    return ans



curr = [1]

for i in range(2, 101):
    curr = prod(curr, i)
    print(curr)

print(sum(curr))
