# range() 함수 실습하기

# 1. range(x) 매개변수 1개짜리 함수를 이용
sum = 0
for x in range(10):
    sum = sum + x
print("1. 0~9까지의 누계 :", sum)

# 2. range(start, stop) 매개변수 2개짜리 함수를 이용
# 누적을 하는데 stop 값은 포함하지 않는다.
sum = 0
for x in range(0, 10):
    sum = sum + x
print("2. 0~9까지의 누계 :", sum)

# 3. range([start], stop, [step]) 매개변수 3개짜리 함수를 이용
# 대괄호 []로 감싸져 있는 매개변수 값은 생략 가능하다라는 것이다.
# 누적을 하는데 stop 값은 포함하지 않는다. 누적을 시킬 때 step 만큼 건너띄어
# 리스트를 생성한다.
sum = 0
for x in range(0, 10, 2):
    sum = sum + x
print("3. 0~9까지의 누계 :", sum)

# 문자열 실습
# 문자열도 시퀀스의 대상에 포함된다. 하여 for 문을 통해 문자를 추출하여 출력할 수 가있다.

s = "Ji Seong Jae"
for ch in s:
    print(ch, end=" ")