from collections import deque

m, n = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]

distance = [[-1] * m for _ in range(n)]
q = deque([(0, 0)])
distance[0][0] = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
while q:
    x, y = q.popleft()
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1:
            if maze[nx][ny] == 0:
                q.appendleft((nx, ny))
                distance[nx][ny] = distance[x][y]
            else:
                q.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1

print(distance[n - 1][m - 1])
