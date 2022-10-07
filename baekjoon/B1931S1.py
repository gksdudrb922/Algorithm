n = int(input())
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))
current_end = meetings[0][1]
result = 1
for start, end in meetings[1:]:
    if start < current_end:
        continue
    else:
        result += 1
        current_end = end

print(result)
