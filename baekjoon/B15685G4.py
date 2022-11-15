n = int(input())
board = [[0] * 101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for _ in range(n):
    x, y, d, g = map(int, input().split())
    dragon_curve = [(x, y), (x + dx[d], y + dy[d])]
    for _ in range(g):
        end = dragon_curve[-1]
        new_dragon_curve = []
        for i in range(len(dragon_curve) - 2, -1, -1):
            a, b = dragon_curve[i]
            na = -b + end[1] + end[0]
            nb = a - end[0] + end[1]
            new_dragon_curve.append((na, nb))
        dragon_curve += new_dragon_curve
    for a, b in dragon_curve:
        board[a][b] = 1

answer = 0
for i in range(100):
    for j in range(100):
        count = 0
        for a, b in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            if board[i + a][j + b] == 1:
                count += 1
        if count == 4:
            answer += 1

print(answer)
