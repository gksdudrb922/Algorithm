# code.plus 코딩 테스트 준비 - 기초 (수학)
MAX = 1000000
dp = [1] * (MAX + 1)
s = [0] * (MAX + 1)
for i in range(2, MAX+1):
    j = 1
    while i * j <= MAX:
        dp[i * j] += i
        j += 1

for i in range(1, MAX + 1):
    s[i] = s[i - 1] + dp[i]

t = int(input())
result = []
for _ in range(t):
    n = int(input())
    result.append(s[n])
print('\n'.join(map(str, result)))
