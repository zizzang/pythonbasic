# 문자열 전달에 대한 실습
# 문자열에 대한 내용도 앞서 살펴본 숫자형의 객체와 동일한 변경될 수 없는
# immutable object 형태이다.
# 파이썬의 경우는 타 언어의 call by value의 개념과는 조금은 다르다.
# 그 이유는 파이썬은 모든 것을 "객체"로 판단을 하기 때문인 것이다.
# 파이썬의 이런 특성이 존재하므로 cally by objective 라고도 칭한다.
def change(string):
    string += "Hello"
    print("change()내의 string 값", string)
    print("change()내의 strig 주소 값", id(string))


msg = "Hi"
print("호출 전 msg 값 : " + msg)
print("호출 전 msg 주소 값", id(msg))
change(msg)
print("호출 후 msg 값 : " + msg)
print("호출 후 msg 주소 값", id(msg))