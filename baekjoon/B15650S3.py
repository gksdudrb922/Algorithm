from itertools import combinations

n, m = map(int, input().split())

data = [i for i in range(1, n + 1)]
for c in list(combinations(data, m)):
    print(' '.join(map(str, c)))
