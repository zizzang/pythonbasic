# 원의 면적과 원의 둘레를 구하는 프로그램을 작성하는데
# PI = 3.141592 전역 상수를 선언하고 상수를 활용하도록 한다.
# circle_area (원의 면적)
# circle_fear (원의 둘레)
# 반지름 radius
# 원의 둘레 = 반지름 x 2 x PI
# 원의 넓이 = 반지름 x 반지름 x PI
import math

# 전역 상수를 선언
PI = 3.141592


# 내 풀이
# def circle(r):
#     circle_area = r * 2 * PI
#     circle_fear = r * r * PI
#     print("원의 면적 : ", circle_area)
#     print("원의 둘레 : ", circle_fear)
#     return


# r = int(input("반지름 입력 : "))
# circle(r)
# circle_area = 0
# circle_fear = 0



# 강사님 풀이

# 프로그램의 시작하는 함수
def main():
    r = float(input("반지름 입력 : "))
    print("반지름이", r, "원의 면적 : ", round(circlearea(r),2))
    print("반지름이", r, "원의 둘레 : ", round(circumference(r),2))

def circlearea(r):
    return PI * r * r

def circumference(r):
    return PI * 2 * r

# 프로그램의 시작을 알리는 함수 호출
main()