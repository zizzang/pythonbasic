# 두 수중 큰 수
def maxint(a, b):
    if a > b:
        return a
    else:
        return b
#  두 수중 큰 수
def get_max(x, y):
    # return 문은 최소화하는게 좋은 코드이다.
    temp = 0        # 최소화 하기 위해서 임시 변수 생성
    if x > y:
        temp = x
    else:
        temp = y
    return temp
# 거듭제곱 구하는 함수
def power(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result