import math

n = int(input())
data = list(map(int, input().split()))

MAX = 1000
is_prime = [True] * (MAX + 1)
for i in range(2, int(math.sqrt(MAX)) + 1):
    if is_prime[i]:
        for j in range(i * 2, MAX + 1, i):
            is_prime[j] = False

primes = set([i for i in range(2, MAX + 1) if is_prime[i]])
result = 0
for x in data:
    if x in primes:
        result += 1

print(result)
