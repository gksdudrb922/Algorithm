e, s, m = map(int, input().split())
answer = 0
temp_e = 0
temp_s = 0
temp_m = 0
while True:
    answer += 1
    if temp_e == 15:
        temp_e = 1
    else:
        temp_e += 1
    if temp_s == 28:
        temp_s = 1
    else:
        temp_s += 1
    if temp_m == 19:
        temp_m = 1
    else:
        temp_m += 1
    if temp_e == e and temp_s == s and temp_m == m:
        break

print(answer)
