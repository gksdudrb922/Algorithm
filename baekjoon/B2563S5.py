n = int(input())
drawing_paper = [[0] * 100 for _ in range(100)]
colored_paper = []
for _ in range(n):
    y, x = map(int, input().split())
    for i in range(x - 1, x + 9):
        for j in range(y - 1, y + 9):
            drawing_paper[i][j] = 1
answer = 0
for i in range(100):
    for j in range(100):
        if drawing_paper[i][j] == 1:
            answer += 1
print(answer)
