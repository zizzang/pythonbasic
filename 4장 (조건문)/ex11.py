# 문자열의 중앙에 있는 문자를 추출해서 출력을 하는 프로그램을 만들기
# 예를 들어서 문자열이 "weekday" 라면 중앙의 문자는 "K"가 된다.
# 하지만, 만약 문자열이 짝수 개의 문자를 가지고 있다면 중앙에 문자를
# 2개의 문자를 출력한다. 예를 들어서 "monday"라면 "nd"를 출력하도록
# 한다.

str_1 = input("문자열을 입력하세요 : ")
length = len(str_1) # 문자열의 길이를 구하고 있는 코드


if (length % 2) == 1:
    ch = str_1[length//2]
    print("중앙에 있는 한 글자는 ", ch)
else:   #문자열의 길이가 짝수라는 것
    ch1 = str_1[length//2 - 1]
    ch2 = str_1[length//2]
    print("중앙에 있는 두 글자는 ", ch1, ch2)
