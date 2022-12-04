n = int(input())
data = [list(input()) for _ in range(n)]
answer = 0
for word in data:
    target = word[0]
    word_set = {target}
    for i in range(1, len(word)):
        if word[i] == target:
            continue
        else:
            if word[i] in  word_set:
                break
            else:
                target = word[i]
                word_set.add(word[i])
    else:
        answer += 1
print(answer)