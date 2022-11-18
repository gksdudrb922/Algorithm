n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

answer = 2 * n * m
for i in range(n):
    total = data[i][0]
    for j in range(1, m):
        d = data[i][j] - data[i][j - 1]
        if d > 0:
            total += d
    answer += 2 * total

for j in range(m):
    total = data[0][j]
    for i in range(1, n):
        d = data[i][j] - data[i - 1][j]
        if d > 0:
            total += d
    answer += 2 * total

print(answer)
