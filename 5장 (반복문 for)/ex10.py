# 터틀 라이브러리를 사용하여 별 모양을 그려보는 프로그램을 for문을 이용하여 작성하시오.

import turtle

t = turtle.Pen()

for i in range(5):
    t.forward(50)
    t.right(145)



# 터틀 크래픽 창이 클릭이 되어야 화면에서 사라지게 하는 코드
turtle.exitonclick()