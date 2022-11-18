n = int(input())

answer = 0
for x in range(1, n + 1):
    sequence = list(map(int, list(str(x))))
    if len(sequence) <= 2:
        answer += 1
        continue
    d = sequence[1] - sequence[0]
    for i in range(1, len(sequence) - 1):
        if sequence[i + 1] - sequence[i] != d:
            break
    else:
        answer += 1

print(answer)
