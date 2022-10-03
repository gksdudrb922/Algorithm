# code.plus 코딩 테스트 준비 - 기초 (수학)
while True:
    try:
        data = 1
        n = int(input())
        while True:
            if data % n == 0:
                print(len(str(data)))
                break
            data = data * 10 + 1
    except EOFError:
        break
