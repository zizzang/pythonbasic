# 두 개의 정수를 입력받아서 두 수 중에서 더 큰 수를 찾아서 큰 수를 리턴하는
# 함수를 만들어보자


# 함수의 목록이 정의되어 있는 모듈을 import 할 때는 항상 개발코드의 상위에
# 위치 할 수 있도록 해야 한다.
from calc import *

#  내 코드
def maxint(a, b):
    if a > b:
        return a
    else:
        return b

x, y = map(int, input().split())
print(maxint(x,y))


# 강사 코드

def get_max(x, y):
    # return 문은 최소화하는게 좋은 코드이다.
    temp = 0        # 최소화 하기 위해서 임시 변수 생성
    if x > y:
        temp = x
    else:
        temp = y
    return temp

# num1 = int(input("첫 번째 숫자 : "))
# num2 = int(input("두 번째 숫자 : "))
# print(num1, "과", num2, "의 값 중에 큰 값은", get_max(num1,num2))



# 거듭제곱을 구하는 코드
num1, num2 = map(int, input().split())
value = power(num1, num2)
print(value)