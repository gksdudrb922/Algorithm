n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
for x, y in sorted(data):
    print(x, y)
