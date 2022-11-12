from collections import deque

n, k = map(int, input().split())

answer_route = []
answer_count = 0
if n >= k:
    answer_route = [i for i in range(n, k - 1, -1)]
    answer_count = n - k
else:
    INF = 100001
    visited = [False] * INF
    q = deque([([n], 0)])
    visited[n] = True

    while q:
        route, count = q.popleft()
        x = route[-1]
        if x == k:
            answer_route = route
            answer_count = count
            break
        for i in [-1, 1]:
            nx = x + i
            if 0 <= nx < INF and not visited[nx]:
                q.append((route + [nx], count + 1))
                visited[nx] = True

        nx = x * 2
        if 0 <= nx < INF and not visited[nx]:
            q.append((route + [nx], count + 1))
            visited[nx] = True

print(answer_count)
print(*answer_route)
