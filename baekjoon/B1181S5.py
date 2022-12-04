import sys

input = sys.stdin.readline
n = int(input())
data = [input().rstrip() for _ in range(n)]

count = [set() for _ in range(51)]
for s in data:
    count[len(s)].add(s)
answer = []
for i in range(1, 51):
    for j in sorted(count[i]):
        answer.append(j)

print('\n'.join(answer))
