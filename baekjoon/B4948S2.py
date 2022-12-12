import math


def count_betrand(n):
    MAX = 2 * n
    is_prime = [False, False] + [True] * (MAX - 1)
    for i in range(2, int(math.sqrt(MAX)) + 1):
        if is_prime[i]:
            for j in range(i * 2, MAX + 1, i):
                is_prime[j] = False
    return len([i for i in range(n + 1, MAX + 1) if is_prime[i]])


answer = []
while True:
    n = int(input())
    if n == 0:
        break
    answer.append(count_betrand(n))

print('\n'.join(map(str, answer)))
