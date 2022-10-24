from curses.ascii import isspace


# 입력받은 문자열의 모든 공백을 제거한 문자열을 출력하는 프로그램을
# 작성하시오.

statements = input("원하는 문자열을 입력하시오 : ")
result = ""

for i in statements:
    # 루프문자가 공백이 아니라면...
    if i != " ":
        result += i        
print(result)