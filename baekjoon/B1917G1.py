def turn(direction):
    global dice
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if direction == 0:
        dice = [d, b, a, f, e, c]
    elif direction == 1:
        dice = [c, b, f, a, e, d]
    elif direction == 2:
        dice = [e, a, c, d, f, b]
    elif direction == 3:
        dice = [b, f, c, d, a, e]
    dice[0] = 1


def dfs(x, y):
    global dice
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < 6 and 0 <= ny < 6 and board[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            turn(direction)
            dfs(nx, ny)
            if direction < 2:
                turn((direction + 1) % 2)
            else:
                turn((direction - 2) % 2 + 3)


answer = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(3):
    board = [list(map(int, input().split())) for _ in range(6)]
    dice = [0] * 6
    visited = [[False] * 6 for _ in range(6)]

    for i in range(6):
        for j in range(6):
            if board[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                dice[0] = 1
                dfs(i, j)

    for d in dice:
        if d == 0:
            answer.append('no')
            break
    else:
        answer.append('yes')

print('\n'.join(map(str, answer)))

'''
14499번 주사위 굴리기에서 응용했다.
'''
