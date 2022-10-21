from itertools import combinations_with_replacement

n, m = map(int, input().split())

data = sorted(list(map(int, input().split())))
for c in list(combinations_with_replacement(data, m)):
    print(' '.join(map(str, c)))
