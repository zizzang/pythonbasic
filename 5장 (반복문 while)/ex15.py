# 사용자로부터 삼풍금액을 입력받아서 상품의 총 가격을 계산하는 프로그램 만들기
# 사용자가 몇 개의 상품을 살지 모르니깐 무한루프를 이용을 하고 아울러 사용자가
# "끝" 이라고 입력을 하면 루프를 탈출하게끔 조건을 주도록 한다.
from operator import eq
total = 0
price = ""
# 무한루프 코드
while True:
    price = input("구입 금액을 입력하시오. ('끝'을 입력하면 종료 됨) : ")
    # '끝'이라는 입력 문구가 있는지 확인하는 코드, 무한 루푸를 탈출하는 코드
    if eq(price, "끝"):     # if price == "끝" 과 동일한 코드  # if perator.eq(price, "끝") 이것도 똑같은 코드
        print("상품의 총 가격 : " + str(total) + "원!")
        break
    total += int(price)


# 클래스 -> 객체
# 클래스의 구성요소
# 1. 멤버변수
# 2. 멤버 함수(메서드)
# 생성자