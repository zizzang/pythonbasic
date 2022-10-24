# 사용자로부터 출력하고 싶은 구구단을 출력하는 프로그램을 만들기

num = int(input("출력하고 싶은 단을 입력하세요 : "))

for i in range (1, 10):
    if (num > 1) and (num < 10):
        print(num, "*", i, "=", (num * i))
    else:
        print("2~9단 위만 계산 가능합니다.")
        break