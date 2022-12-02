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

    nx = x * 2
    if 0 <= nx < INF and not visited[nx]:
        q.append((nx, count))
        visited[nx] = True

    for i in [-1, 1]:
        nx = x + i
        if 0 <= nx < INF and not visited[nx]:
            q.append((nx, count + 1))
            visited[nx] = True

print(answer)

'''
숨바꼭질1(B1697S1)에서 1 -> 2가 되는 경우 고려 (2 * x를 더 앞에 둔다)
'''