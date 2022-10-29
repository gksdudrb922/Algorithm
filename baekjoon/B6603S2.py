from itertools import combinations

while True:
    data = list(map(int, input().split()))
    k = data[0]
    if k == 0:
        break
    s = data[1:]
    for c in list(combinations(s, 6)):
        print(*c)
    print()
