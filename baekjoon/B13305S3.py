n = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

current_cost = cost[0]
result = current_cost * distance[0]
for i in range(1, n - 1):
    if cost[i] < current_cost:
        current_cost = cost[i]
    result += current_cost * distance[i]

print(result)
