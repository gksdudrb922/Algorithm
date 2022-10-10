n = int(input())
data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append((x, y))

answer = []
for x, y in data:
    rank = 1
    for p, q in data:
        if x < p and y < q:
            rank += 1
    answer.append(rank)

print(" ".join(map(str, answer)))
