import math

m, n = map(int, input().split())
is_prime = [False, False] + [True] * (n - 1)
for i in range(2, int(math.sqrt(n)) + 1):
    if is_prime[i]:
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
primes = [i for i in range(m, n + 1) if is_prime[i]]
print('\n'.join(map(str, primes)))
