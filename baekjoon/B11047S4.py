n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

result = 0
for i in range(len(coins) - 1, -1, -1):
    coin = coins[i]
    if coin <= k:
        result += k // coin
        k %= coin
    if k == 0:
        break

print(result)
