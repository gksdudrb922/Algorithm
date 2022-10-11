n = int(input())
board = []
for _ in range(n):
    board.append(list(input()))


def print_board(b):
    for i in range(n):
        for j in range(n):
            print(b[i][j], end='')
        print()


def check_score(b):
    result = 1
    for i in range(n):
        target = b[i][0]
        score = 1
        for j in range(1, n):
            if target == b[i][j]:
                score += 1
            else:
                result = max(result, score)
                target = b[i][j]
                score = 1
        result = max(result, score)
    for j in range(n):
        target = b[0][j]
        score = 1
        for i in range(1, n):
            if target == b[i][j]:
                score += 1
            else:
                result = max(result, score)
                target = b[i][j]
                score = 1
        result = max(result, score)
    return result


dx = [0, 1]
dy = [1, 0]
answer = 0
for x in range(n):
    for y in range(n):
        for direction in range(2):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < n and board[x][y] != board[nx][ny]:
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                answer = max(answer, check_score(board))
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

print(answer)
