n = int(input())
data = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if data[i - 1] > data[i]:
        a = i - 1
        break
else:
    print(-1)
    exit(0)

for i in range(n - 1, 0, -1):
    if data[a] > data[i]:
        b = i
        break

data[a], data[b] = data[b], data[a]
data = data[:a + 1] + sorted(data[a + 1:], reverse=True)
print(' '.join(map(str, data)))
