from itertools import combinations_with_replacement

n, m = map(int, input().split())

data = [i for i in range(1, n + 1)]
for c in list(combinations_with_replacement(data, m)):
    print(' '.join(map(str, c)))
