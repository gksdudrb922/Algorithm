n, s = map(int, input().split())
data = list(map(int, input().split()))

answer = 0
for subset in range(1, 1 << n):
    total = 0
    for i in range(n):
        if subset & (1 << i):
            total += data[i]
    if total == s:
        answer += 1

print(answer)
