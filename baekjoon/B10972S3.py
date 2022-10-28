n = int(input())
data = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if data[i - 1] < data[i]:
        a = i - 1
        break
else:
    print(-1)
    exit(0)

for i in range(n - 1, 0, -1):
    if data[a] < data[i]:
        b = i
        break

data[a], data[b] = data[b], data[a]
data = data[:a + 1] + sorted(data[a + 1:])
print(' '.join(map(str, data)))

'''
1. 오름차순이 나오는 순간의 i - 1을 저장
2. i - 1 보다 큰 값을 저장
3. 둘을 swap
4. swap 이후부터는 sorting
(주의) N = 10 이상이면 permutations(data, n) 호출 시 256MB 초과
'''