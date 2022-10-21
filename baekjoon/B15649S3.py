from itertools import permutations

n, m = map(int, input().split())

data = [i for i in range(1, n + 1)]
for p in list(permutations(data, m)):
    print(' '.join(map(str, p)))
