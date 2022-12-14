# 반복문에(interation0)에 대한 실습
# 아래와 같이 "안녕하세요"를 5번 출력하려면 print()를 5번 호출해야하 하는
# 번거로움이 존재하며, 아울러 1000번 이상 출력을 한다면 정말 짜증날 것이다.

# 안녕하세요
# 안녕하세요
# 안녕하세요
# 안녕하세요

# 위의 출력내용과 동일하게 for 문을 이용하여 작성해보자.
# 아래는 for 문을 이용하여 출력한 코드인데 여기서 x를 루프변수라 칭하며
# in 다음에 오는 것을 시퀀스라고 칭한다.
# 시퀀스에 올 수 있는 것은 리스트, 문자열이 존재한다.
# 아래 코드는 for 문을 사용헀지만 정수 리스트를 시퀀스로 만들었기 때문에
#  1000번의 루프를 하게 만들려면 정수 리스트가 1000개의 값이 존재해야
# 하는 또 다른 번거로움이 생긴다.
for x in [0, 1, 2, 3, 4]:
    print("안녕하세요.")
    

print("-------------")
# range(x)를 이용하면 위의 정수 리스트를 사용하는 것보다 훨씬 효율적인 코드이며
# 아울러 가독성도 좋다. range() 함수는 리스트 타입으로 반환해준다.
# rage(x) : 0부터 시작하고 마지막 값 (5-1)까지 정수 리스트 타입으로 반환을 
# 해준다.
for x in range(5):
    print("안녕하세요.")
# 그리고 range()  함수의 타입은 range 객체타입이다.
print(type(range(5)))

# 문자열 리스트를 시퀀스로 가질 때의 for 문
s = ["지성재", "코알라", "돌고래", "팬더"]
for name in s:
    print("반갑습니다." + name + "님!")

#  줄바꿈을 하지 않게 하는 end 인자갑을 확인해보기
for x in [0, 1, 2, 3, 4]:
    print(x, end="\t")