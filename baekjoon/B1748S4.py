n = int(input())

n_length = len(str(n))
answer = 0
for i in range(1, n_length):
    answer += 9 * 10 ** (i - 1) * i
answer += (n - (10 ** (n_length - 1)) + 1) * n_length

print(answer)
                                             