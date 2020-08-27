def is_prime(x):
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1
    return x > 1

def process(x, nums):
    if x > 10:
        nums.append(x)

    for d in range(1, 10):
        y = x*10 + d

        if is_prime(y):
            process(y, nums)

nums = []
for x in range(2, 10):
    if is_prime(x):
        process(x, nums)

print(nums)

truncs = []
for x in nums:
    y = x
    print(f'processing: {y}')

    isOK = True
    while y > 10 and isOK:
        y = int(str(y)[1:])
        isOK &= is_prime(y)
        print('\t', isOK, y)

    if isOK:
        truncs.append(x)

print(truncs)
print(f'Answer: {sum(truncs)}')
