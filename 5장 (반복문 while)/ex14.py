# 임의의 숫자를 발생시켜 숫자를 맞추는 게임을 만들어보기

from random import *

cnt = 0
num = randint(1, 100)

print ("발생한 난수의 값 : ", num)
print("1부터 100사이의 숫자를 맞추어 보세요.")
print("기회는 단 10번 입니다.")

while cnt < 10:
    guess = int(input("숫자를 입력하시오. : "))
    cnt += 1
    if num == guess:
        print("숫자를 맞추셨습니다. 시도횟수 :", cnt)
        code = input("게임을 계속 하시겠습니까 ?(Y/N) ")
        if code == "Y":
            print("------------------")
            # 게임을 재시작 하기 위해서 난수가 다시 발생 하며, cnt를 초기화를 해야 한다.
            print("게임을 재시작합니다.")
            num = randint(1, 100)
            print ("발생한 난수의 값 : ", num)
            cnt = 0
        if code == "N":     #게임 종료 코드
            print("게임을 종료합니다.", "시도횟수", cnt)
            break 
    elif num > guess:
        print("숫자가 보다 큽니다.") 
    elif num < guess:
        print("숫자가 보다 작습니다.")