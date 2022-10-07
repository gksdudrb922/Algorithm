expression = input().split('-')

result = 0
for i in range(len(expression)):
    s = 0
    for x in expression[i].split('+'):
        s += int(x)
    if i == 0:
        result += s
    else:
        result -= s

print(result)
