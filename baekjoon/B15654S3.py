from itertools import permutations

n, m = map(int, input().split())

data = sorted(list(map(int, input().split())))
for p in list(permutations(data, m)):
    print(' '.join(map(str, p)))
