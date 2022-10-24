# 1) 반복문은 중첩하여 사용될 수 있다. 즉 반복문 안에 다른 반복문이 포함될 수 있다.
# 2) 중첩 반복문은 > nested loop
# 3) 그 안의 외부 반복문 > outer loop
# 4) 그 안의 내부 반복문 > inner loop
# 5) ! 중요한것은 내부 반복문은 외부 반복문이 한번 반복할 떄마다 새롭게 실행된다는 점이다.
# 6) 중첩반복문은 실제 프로그래밍에서 자주 등장한다.
# 7) 테이블과 비슷한 데이터를 처리할 하는데 유용

# 8)ex    ****************
#         ****************
#         ****************
#         ****************
#         ****************
# for y in range(5):
#     for x in range(10):
#         print("*",end="")
#     print("")

# 9) 반복문으로 문자열 처리하기
# 문자열도 시퀀스의 일종이라는 것이다.
# fruit = "apple"
# for letter in fruit:
#     print(letter, end=" ")

# 10)
# 반복문의 문자열 처리 예제
# s = input("문자열을 입력하시오 : ")
# vowels = "aeiouAEIOU" # 영문의 모음 리스트를 문자열로 저장
# result = ""
# for letter in s:
#     if letter not in vowels:
#         result += letter
# print(result) ## 모음을 제외한 문자는 없이 정해진 자음만 출력 됨


