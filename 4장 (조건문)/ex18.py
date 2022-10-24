# 주사위 눈을 랜덤으로 발생시켜서 해당하는 숫자를 출력하는 프로그램을 만들기
#  randint() 함수를 검색하여 사용법을 익힌 후 프로그램을 작성하시오.

from random import *
# randint(a, b) 함수는 a 부터 b 까지의 사이에 있는 정수를 반환해주는 함수
num = randint(1, 6)
print("주사위 눈 : ", num)

# random() 함수는  0.0부터 1.0미만의 임의의 값을 float 형태로 반환해주는 함수
num = random()
print("num : ", num)

# randrange(start, stop, step) > 함수는 start에서 stop 까지 2단계 씩
num = randrange(0, 101, 1)
print("num : ", num)

# randint(a, b) 함수는 a 부터 b 까지의 사이에 있는 정수를 반환해주는 함수
if num == 1:
    print("주사위 눈 : 1")
elif num == 2:
    print("주사위 눈 : 2")
elif num == 3:
    print("주사위 눈 : 3")
elif num == 4:
    print("주사위 눈 : 4")
elif num == 5:
    print("주사위 눈 : 5")
else:
    print("주사위 눈 : 6")