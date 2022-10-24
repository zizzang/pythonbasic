# 리스트 함축
# 파이썬은 "리스트함축 (list comprehensions)" 또는 "리스트 컴프리헨션" 이라는 개념을 지원한다.
# comprehension은 함축, 포함 , 내포 라는 의미이다.
# ''리스트 함축은 수학자들이 집함을 정의하는 것과 유사하다.''
# ex) s = [ x**2 for x in range(10) ]
# x는 입력 리스트의 요소를 나타내는 변수이다.
# x**2는 출력식으로서 새로운 리스트의 요소를 생성한다.
# range(10)은 입력 리스트를 나타낸다.
# [...]은 결과가 새로운 리스트라는 것을 의미한다.


# 조건이 붙는 리스트 함축
# ex) 짝수의 집합
M = [x for x in range(10) if x % 2 == 0]
print(M)


# 다양한 자료형에 대한 리스트 함축(1)
# 리스트 함축은 숫자에 대해서만 적용되는 것은 아니다. 어떤 자료형에 대해서도 리트스 함축을 적용할 수
# 있다. 단어를 저장하는 리스트를 가정하자. 단어의 첫 글자만을 추출하여 리스트로 만드는 문장을 만든다.
list = ["ALL", "good", "things", "must", "come", "to", "an", "end"]
items = [word[0] for word in list]
print(items)
# 다양한 자료형에 대한 리스트 함축(2)
# 단어의 길이를 계산하고 이것을 리스트로 생성
word_list = "Doncount your chickens before they are hatched".split(" ")
result_list = [len(w) for w in word_list]
print(result_list)


# 상호곱(Cross product = 카디션 곱) 형태의 집합
# 리스트 함축은 2개의 집합의 상호곱 형태로도 표현할 수 있다. 예를 들어서 색상의 집합과 자동차의 집합을 상호
# 곱하여 새로운 리스트를 생성할 수 있다.
# 아래 코드는 colors 리스트의 원소와 cars 리스트의 원소가 하나씩 짝지어져서 튜플이 되고 이 튜플이 모여서
# 리스트가 된다.
colors = ["white", "silver", "black"]
cars = ["bmw5", "sonata", "maliub", "sm6"]
colored_cars = [(x,y) for x in colors for y in cars]
print(colored_cars)


