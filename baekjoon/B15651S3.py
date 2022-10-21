from itertools import product

n, m = map(int, input().split())

data = [i for i in range(1, n + 1)]
for p in list(product(data, repeat=m)):
    print(' '.join(map(str, p)))
