k = int(input())
data = input().split()


def dfs(num):
    global min_answer, max_answer
    count = len(num)
    if count == k + 1:
        min_answer = min(min_answer, int(num))
        max_answer = max(max_answer, int(num))
        return

    for i in range(10):
        if not visited[i]:
            if (count == 0) or (data[count - 1] == '<' and int(num[-1]) < i) or (
                    data[count - 1] == '>' and int(num[-1]) > i):
                visited[i] = True
                dfs(num + str(i))
                visited[i] = False


visited = [False] * 10
min_answer = int(1e10)
max_answer = 0
dfs("")
print('0' + str(max_answer) if len(str(max_answer)) != k + 1 else str(max_answer))
print('0' + str(min_answer) if len(str(min_answer)) != k + 1 else str(min_answer))
