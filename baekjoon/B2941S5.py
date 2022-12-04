croatia = {"c=", "c-", "d-", "lj", "nj", "s=", "z="}
data = input()
n = len(data)
answer = 0
i = 0
while i < n:
    answer += 1
    if i < n - 1 and data[i:i + 2] in croatia:
        i += 2
    elif i < n - 2 and data[i:i + 3] == "dz=":
        i += 3
    else:
        i += 1
print(answer)
