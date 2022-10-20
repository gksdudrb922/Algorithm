def dfs(x, y, count, total):
    global answer
    if answer >= total + max_val * (4 - count):
        return
    if count == 4:
        answer = max(answer, total)
        return
    else:
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, count + 1, total + board[nx][ny])
                visited[nx][ny] = False


def not_dfs(x, y, total):
    global answer
    count = 0
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < m:
            count += 1
            total += board[nx][ny]

    if count == 3:
        answer = max(answer, total)
    elif count == 4:
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            total -= board[nx][ny]
            answer = max(answer, total)
            total += board[nx][ny]


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
max_val = max(map(max, board))
answer = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        not_dfs(i, j, board[i][j])
        visited[i][j] = False

print(answer)
