from itertools import combinations

n, m = map(int, input().split())

data = sorted(list(map(int, input().split())))
for c in list(combinations(data, m)):
    print(' '.join(map(str, c)))
