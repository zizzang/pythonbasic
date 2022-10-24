# 사용자에게 명령어를 입력받아서 터틀그래픽을 제어를 해보자. 즉 사용자가 "left"를 입력을
# 하면 왼쪽으로 회전하게 되고 사용자가 "right"를 입력 했다면 오른쪽으로 회전하게 하는
# 프로그램 만들기

import tkinter
tkinter.Tk()
import turtle

# 펜의 기능을 t라는 변수에 저장함.
t = turtle.pen()
# 반복문을 무한루프를 돌려서 if 구문을 이용하여 방향을 제어하는 코드
# 무한루프를 프로그래밍을 했다면 반드시 루프를 탈출하는 코드가 반드시 있어야 된다.(중요)

while True:
    direction = input("왼쪽=left, 오른쪾=right, 종료=quit")
    # break 는 무한루푸를 빠져나가라
    if direction == "quit":
       break 
    # 사용자가 left 를 입력했을때
    if direction == "left":
        t.left(60)
        t.forward(50)
    if direction == "right":
        t.right(60)
        t.forward(50)
