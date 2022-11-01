n, m = map(int, input().split())
data = [list(map(int, input())) for _ in range(n)]

answer = 0
for i in range(1 << n * m):
    total = 0
    for row in range(n):
        row_sum = 0
        for col in range(m):
            index = row * m + col
            if i & (1 << index) != 0:
                row_sum = row_sum * 10 + data[row][col]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum

    for col in range(m):
        col_sum = 0
        for row in range(n):
            index = row * m + col
            if i & (1 << index) == 0:
                col_sum = col_sum * 10 + data[row][col]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum
    answer = max(answer, total)

print(answer)
