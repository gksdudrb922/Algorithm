n, m, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

answer = -10000
visited = [[False] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(bx, by, count, total):
    global answer
    if count == k:
        answer = max(answer, total)
        return

    for x in range(bx, n):
        for y in range(by if x == bx else 0, m):
            if visited[x][y]:
                continue
            near_flag = False
            for direction in range(4):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                    near_flag = True
                    break

            if not near_flag:
                visited[x][y] = True
                dfs(x, y, count + 1, total + board[x][y])
                visited[x][y] = False


dfs(0, 0, 0, 0)
print(answer)
