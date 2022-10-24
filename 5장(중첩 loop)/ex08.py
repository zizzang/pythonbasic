# 입력받은 문자열을 거꾸로 출력하는 프로그램을 작성하시오.
from re import S


statements = input("문자열을 입력하세요 : ")
s_reverse = ""


# for 문을 활용한 방법
for ch in statements:
    s_reverse = ch + s_reverse  # 복합대입연사자로 하면 안됨

print("입력한 문자열 : " + statements)
print("역순으로 출력한 문자열 :" + s_reverse)

print("------------------------------------")
# list() 함수는 문자열을 리스트 타입으로 바꾸는 함수이다.

s_list = list(statements)
# print(type(s_list))
# reverse() 는 리스트 타입을 역순으로 바꿔주는 함수이다.
s_list.reverse()
# join() 함수는 역순으로 된 문자열을 연결해서 출력을 하고 있는 코드
print("".join(s_list))

print("------------------------------------")
s1 = statements
# reversed() 는 문자열을 역순으로 하는 함수
print("".join(reversed(s1)))

# 파이썬에서는 [::-1]를 사용해서 문자열을 역순으로 출력할 수 있다.
print("------------------------------------")
print(statements[::-1])
print("------------------------------------")
print(statements[3::-1])