n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))

answer = 32
for x in range(n - 7):
    for y in range(m - 7):
        b_count = 0
        w_count = 0
        for i in range(x, x + 8):
            for j in range(y, y + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] == 'B':
                        w_count += 1
                    else:
                        b_count += 1
                else:
                    if board[i][j] == 'B':
                        b_count += 1
                    else:
                        w_count += 1
        answer = min(answer, min(b_count, w_count))

print(answer)
