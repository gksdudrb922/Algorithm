data = [0] * 11
data[1], data[2], data[3] = 1, 2, 4
for i in range(4, len(data)):
    data[i] = data[i - 1] + data[i - 2] + data[i - 3]

t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    answer.append(data[n])

print('\n'.join(map(str, answer)))
