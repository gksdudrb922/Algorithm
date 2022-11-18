from collections import deque

s = int(input())

MAX = 2 * s + 1
visited = [[False] * MAX for _ in range(MAX)]
q = deque([(1, 0, 0)])
visited[1][0] = True
answer = 0
while q:
    count, clip_board, t = q.popleft()
    if count == s:
        answer = t
        break
    if not visited[count][count]:
        q.append((count, count, t + 1))
        visited[count][count] = True
    if count < count + clip_board < MAX and not visited[count + clip_board][clip_board]:
        q.append((count + clip_board, clip_board, t + 1))
        visited[count + clip_board][clip_board] = True
    if count - 1 >= 1 and not visited[count - 1][clip_board]:
        q.append((count - 1, clip_board, t + 1))
        visited[count - 1][clip_board] = True

print(answer)
