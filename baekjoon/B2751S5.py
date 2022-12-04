import sys

input = sys.stdin.readline
n = int(input())
data = [int(input()) for _ in range(n)]
for x in sorted(data):
    print(x)
    