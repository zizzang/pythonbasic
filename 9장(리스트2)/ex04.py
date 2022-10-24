# 리스트 함축
# 리스트 함축은 수학에서 집합을 정의하는 것과 매우 유사하다.

# 일반적 코드(리스트 함축을 사용하지 않은 경우)
# squares = []
# for x in range(1, 11):
#     squares.append(x **2)
# print(squares)

# 리스트 함축 개념을 이용하여 위와 똑같은 결과 출력하기
# 위의 일반적인 코드보다 코드가 간결하고 쉽게 리스트를 생성 가능하다.
# 리스트 함축 반복문 문법 : 출력식 반복문 조건문(옵션)
# li_squares = [x**2 for x in range(1, 11)]
# print(li_squares)


# 조건이 붙는 리스트 함축(조건문 if 를 사용하겠다)
# 조건식이 참이 되는 것만 리스트 요소로 생성시킨다.
# odd_list = [x for x in range(1, 21) if x % 2 == 1]
# print(odd_list)

# for 반복문 2개를 사용하여 구구단의 값을 출력해보자
gg_list = [ i*j for i in range(2, 10) for j in range(2, 10) ]

# 아래와 같이 하면 가독성이 좋음
# gg_list = [ i*j for i in range(2, 10)
                # for j in range(2, 10) ]
print(gg_list)

# 문자열에 대한 리스트 함축
# 문자열의 첫 번째 문자만 가지는 리스트를 생성하능 예제
list1 = ["korea", "대한민국", "서울특별시", "한라산", "END"]
first_word = [word[0] for word in list1]
print("단어의 첫 문자 : ", first_word)
# 문자열의 마지막 번째 문자만 가지는 리스트를 생성하능 예제
list1 = ["korea", "대한민국", "서울특별시", "한라산", "END"]
first_word = [word[len(word)-1] for word in list1]
print("단어의 끝 문자 : ", first_word)

# 단어의 길이 가지는 리스트를 생성하능 예제
list1 = ["korea", "대한민국", "서울특별시", "한라산", "END"]
first_word = [len(word) for word in list1]
print("단어의 끝 문자 : ", first_word)

# 상호곱(Cross Product) = 카티션 곱이랑 비슷한 내용
colors = ["흰색", "브라운색", "검정색"]
cars = ["그랜져", "소나타", "스파크", "아반떼", "봉고"]
colors_cars = [ x+"-"+y for x in colors
                        for y in cars ]
print("색상과 차종 : ", colors_cars)