import math

MAX = 1000000
is_prime = [False, False] + [True] * (MAX - 1)
for i in range(2, int(math.sqrt(MAX)) + 1):
    if is_prime[i]:
        for j in range(i * 2, MAX + 1, i):
            is_prime[j] = False
primes = [i for i in range(2, MAX + 1) if is_prime[i]]
prime_set = set(primes)

result = []
while True:
    n = int(input())
    if n == 0:
        break
    prime_flag = False
    for a in primes:
        if n - a in prime_set:
            prime_flag = True
            result.append(str(n) + " = " + str(a) + " + " + str(n - a))
            break
    if not prime_flag:
        result.append("Goldbach's conjecture is wrong.")

print('\n'.join(result))
