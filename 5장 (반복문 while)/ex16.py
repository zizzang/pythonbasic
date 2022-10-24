# 플래그 변수를 사용한 무한 루프 문제
# 1. 증속, 2. 감속 3. 중지 를 출력하고 사용자의 입력을 1, 2, 3 으로 받아서
# 증속을 하면 속도를 10씩 증가시키고 출력해준다.
# 감속을 하면 속도를 10씩 감소시키고 출력해준다.
# 중지를 하면 플래그 변수를 이용하여 무한 루프를 빠져나간다.

run = True
speed = 0
KeyCode = 0


while run:
    print("---------------------------")
    print("1. 증속 | 2. 감속 | 3. 중지")
    print("---------------------------")
    KeyCode = int(input("선택 : "))
    
    # 증속의 경우
    if KeyCode == 1:
        speed += 10
        print("현재 속도 : ", speed)
    # 감속의 경우
    elif KeyCode == 2:
        speed -= 10
        if speed < 0:
            print("속도가 음수 값 입니다.")
            speed = 0
        else:
            print("현재 속도 : ", speed)
    # 중지의 경우 (중지일 경우 플래그 변수를 False로 설정해줌으로써 무한 루프를 탈출 하는 코드)
    elif KeyCode == 3:
        print("중지 되었습니다.")
        run = False
    # 사용자가 잘못 입력했을 경우
    else:
        print("잘못된 입력값입니다.")
