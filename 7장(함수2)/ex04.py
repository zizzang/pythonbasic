# mutable object 중 dictionary 라는 타입이 있다.
# 딕셔너리라는 타입의 형태는 키와 값의 쌍으로 이루어져 있다.
# Key와 Value가 쌍을 이루는 구죠
# Key 변경할 수 없음 Unique 함 또한, dictionary안에 key의 값은 유일 해야함
# Value 값은 변경 할 수 있음
# 딕셔너리의 call by reference 가 성립되는 이유는 변경 가능한 mutable object
# 이기 때문에 가능한 것이다. call by objective-reference 라고도 칭한다.

def change(dic):
    print("change()함수 내의 연산전의 dic의 값 : ", dic)
    print("change()함수 내의 연산전의 dic의 주소 값 : ", id(dic))
    dic["몸무게"] = 42
    print("change()함수 내의 연산후의 dic의 값 : ", dic)
    print("change()함수 내의 연산전의 dic의 값 : ", id(dic))


dic = {"name":"코알라", "age":14, "height":160}
print("호출전의 dic의 값 : ", dic)
print("호출전의 dic의 주소 값 : ", id(dic))
change(dic)
print("호출후의 dic의 값 : ", dic)
print("호출후의 dic의 주소 값 : ", id(dic))



