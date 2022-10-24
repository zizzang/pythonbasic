from math import *

# 파이썬에서의 자료형(Data-type)
# int형을 출력해봄
print(type(17))
# float형을 확인해봄
print(type(10.77779))
# str 형을 출력해봄 
print(type("안녕하세요."))




# 반지름이 r인 구의 부피는 4/3 * PI * r의 세제곱
# 반지름이 5인 구의 부피를 계산하는 프로그램
# math 라이브러리 import
# pow > 제곱 수 구할 수 있음
r = 5.0
volume = 4.0/3.0 * pi * pow(r, 3)
print("구의 부피 : " , volume)
# 문자열 + float 은 타입이 일치가 안되어 문자열을 생성할 수 없음, 아래와 같이 맞춰 줘야 함
# 해결하기 위한 방안은 문자열 즉 숫자로 변환이 되지 않는 문자열에다가 int()를
# 사용하면 error 를 발생시키고, 아울러 + 연산이 이루어지지 않음을 알 수가  
# 있다. 하여 이때는 실수 값을 str()를 이용하여 문자열로 변환을 하면 + 연산이 이루어진다
print("구의 부피 : " + str(volume))


# 구의 겉넓의 공식 : 4*pi*r의 제곱
outer_area = 4 * pi * pow(r, 2)
print("구의 겉넓이 : " + str(outer_area))
print("구의 겉넓이 : " , outer_area)