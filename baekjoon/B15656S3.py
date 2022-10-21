from itertools import product

n, m = map(int, input().split())

data = sorted(list(map(int, input().split())))
for p in list(product(data, repeat=m)):
    print(' '.join(map(str, p)))
