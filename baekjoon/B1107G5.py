n = int(input())
m = int(input())
fault_button = list(map(int, input().split())) if m > 0 else []

answer = abs(n - 100)
for i in range(1000001):
    fault_flag = False
    for button in fault_button:
        if str(button) in str(i):
            fault_flag = True
            break
    if not fault_flag:
        answer = min(answer, len(str(i)) + abs(n - i))

print(answer)
