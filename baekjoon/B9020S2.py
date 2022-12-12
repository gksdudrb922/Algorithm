import math

MAX = 10000
is_prime = [False, False] + [True] * (MAX - 1)
for i in range(2, int(math.sqrt(MAX)) + 1):
    if is_prime[i]:
        for j in range(i * 2, MAX + 1, i):
            is_prime[j] = False
primes = [i for i in range(2, MAX + 1) if is_prime[i]]
prime_set = set(primes)

t = int(input())
for _ in range(t):
    n = int(input())
    goldbach_partitions = []
    for prime in primes:
        if prime > n // 2:
            break
        if n - prime in prime_set:
            goldbach_partitions.append((prime, n - prime, abs(2 * prime - n)))
    goldbach_partitions.sort(key=lambda x: x[2])
    print(goldbach_partitions[0][0], goldbach_partitions[0][1])
