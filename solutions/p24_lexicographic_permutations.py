from itertools import permutations

L = list(range(10))
perms = list(permutations(L))[999999]
print(perms)
