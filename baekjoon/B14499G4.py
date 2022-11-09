from collections import deque

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))

cq = deque([0, 0, 0, 0])
rq = deque([0, 0, 0])
answer = []
for c in command:
    if c == 1 and y + 1 < m:
        y += 1
        rq.rotate(1)
        cq[1] = rq[1]
        rq[0], cq[3] = cq[3], rq[0]
    elif c == 2 and y - 1 >= 0:
        y -= 1
        rq.rotate(-1)
        cq[1] = rq[1]
        rq[2], cq[3] = cq[3], rq[2]
    elif c == 3 and x - 1 >= 0:
        x -= 1
        cq.rotate(-1)
        rq[1] = cq[1]
    elif c == 4 and x + 1 < n:
        x += 1
        cq.rotate(1)
        rq[1] = cq[1]
    else:
        continue
    if board[x][y] == 0:
        board[x][y] = cq[3]
    else:
        cq[3] = board[x][y]
        board[x][y] = 0
    answer.append(cq[1])

print('\n'.join(map(str, answer)))
