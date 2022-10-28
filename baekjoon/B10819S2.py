from itertools import permutations

n = int(input())
data = list(map(int, input().split()))

data_permutations = list(permutations(data, n))
answer = -1000
for p in data_permutations:
    total = 0
    for i in range(n - 1):
        total += abs(p[i] - p[i + 1])
    answer = max(answer, total)

print(answer)
