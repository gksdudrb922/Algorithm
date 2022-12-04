import sys

input = sys.stdin.readline
n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
for x, y in sorted(data, key=lambda x: (x[1], x[0])):
    print(x, y)
