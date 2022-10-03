# code.plus 코딩 테스트 준비 - 기초 (수학)
n = int(input())
g = 0
for i in range(1, n + 1):
    g += n // i * i
print(g)
