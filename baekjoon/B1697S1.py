from collections import deque

n, k = map(int, input().split())

INF = 100001
visited = [False] * INF
q = deque([(n, 0)])
visited[n] = True
answer = 0
while q:
    x, count = q.popleft()
    if x == k:
        answer = count
        break
    for i in [-1, 1]:
        nx = x + i
        if 0 <= nx < INF and not visited[nx]:
            q.append((nx, count + 1))
            visited[nx] = True

    nx = x * 2
    if 0 <= nx < INF and not visited[nx]:
        q.append((nx, count + 1))
        visited[nx] = True

print(answer)
