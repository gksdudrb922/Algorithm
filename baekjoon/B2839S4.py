n = int(input())
d = [5001] * (n + 1)
d[0] = 0
for i in [3, 5]:
    for j in range(i, n + 1):
        d[j] = min(d[j], d[j - i] + 1)
print(d[n] if d[n] != 5001 else -1)
