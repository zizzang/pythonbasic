# 함수(function)에 대한 실습
# 1. 함수는 프로그램 안에서 중복된 코드를 제거한다.
# 2. 복잡한 프로그래밍 작업을 더 간단한 작업들로 분해할 수 있다.
# 3. 함수는 한번 만들어두면 재사용이 얼마든지 가능하다.
# 4. 함수를 사용하면 가독성이 증대되고, 유지관리도 쉬워진다.

# 간단한 함수

# 아래는 파일안의 모든 내용을 가져오기 때문에 파일이름.함수명으로 접근할 필요가 없다.
# from ex01module import *



# 아래는 파일명.함수명으로 접근해야 한다.
# import ex01module

# def say_hello(name):            # 함수의 선언부 = 헤더
#     print("안녕하세요," + name)  # 함수의 구현부 = 바디

# ex01module.say_hello("지성재")             # Call
# ex01module.say_hello("코알라")             # Call

# 파이썬에서는 오버로딩의 개념이 없다. 같은 함수의 이름이라면 마지막에 정의된
# 함수만 인식하게 된다. 하여, 함수명은 유니크한 값으로 함수명을 짓도록 한다.
# def say_hello(name, msg):
#     print("안녕하세요,", name, msg)


# ex01module.say_hello_msg("돌고래", "도와주세요")
# 위와 같이 함수를 정의만 했다면 출력값은 없다. 출력값이 나오게 하려면
# 호출(call)을 해야한다.



# 아래는 함수가 호출되어 10을 출력을 하긴 하지만 가독성이 좋지않다.
# 이유는 함수의 매개변수명이 name 이니 웬만하면 이름을 매개변수 값으로 주는
# 것이 현명한 코드가 될 것이다.
# say_hello(10)


# 값을 반환(return)하는 함수 예제
# start 부터 end 까지의 누적합을 구하는 함수
def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

# get_sum()을 이용하여 범위값의 누적합을 구하는 코드
result = get_sum(1, 10)
print(type(result))
print(result)


result = get_sum(1, 100)
print(type(result))
print(result)

    