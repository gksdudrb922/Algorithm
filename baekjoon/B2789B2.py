from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

card_combi = list(combinations(data, 3))
result = 0
for card in card_combi:
    s = sum(card)
    if 0 <= m - s <= m - result:
        result = s

print(result)
