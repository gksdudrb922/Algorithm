n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer = 0
clean = [[False] * m for _ in range(n)]
while board[r][c] == 0:
    if not clean[r][c]:
        clean[r][c] = True
        answer += 1
    for i in range(4):
        d = 3 if d == 0 else d - 1
        nr = r + dr[d]
        nc = c + dc[d]
        if board[nr][nc] == 0 and not clean[nr][nc]:
            r, c = nr, nc
            break
    else:
        if d % 2 == 0:
            r -= d - 1
        else:
            c += d - 2

print(answer)
