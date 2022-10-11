from itertools import combinations

dwarf = []
for _ in range(9):
    dwarf.append(int(input()))

dwarf_combi = list(combinations(dwarf, 7))
for dwarf_heights in dwarf_combi:
    if sum(dwarf_heights) == 100:
        answer = sorted(dwarf_heights)

print('\n'.join(map(str, answer)))
