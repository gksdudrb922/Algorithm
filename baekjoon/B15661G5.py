n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]


def get_ability_diff(team):
    start = 0
    for i, x in enumerate(team[:-1]):
        for y in team[i + 1:]:
            start += s[x][y] + s[y][x]

    link = 0
    another_team = list(set(range(n)) - set(team))
    for i, x in enumerate(another_team[:-1]):
        for y in another_team[i + 1:]:
            link += s[x][y] + s[y][x]

    return abs(start - link)


def dfs(team):
    global answer

    for i in range(team[-1] + 1 if team else 0, n):
        if team and team[0] != 0:
            return
        team.append(i)
        answer = min(answer, get_ability_diff(team))
        if answer == 0:
            print(answer)
            exit(0)
        dfs(team)
        team.pop()


answer = 10000
dfs([])
print(answer)
