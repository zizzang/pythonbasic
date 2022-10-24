statements = "      안녕!"
# 왼쪽 공백만 제거하는 함수(lstrip())
print(statements.lstrip())


statements = "안녕!      "
# 오른쪽 공백만 제거하는 함수(lstrip())
print(statements.rstrip())



statements = "     안녕!      "
# 양쪽 제거하는 함수(lstrip())
print(statements.strip())



# 문자열 나누기
print("---------------------------------------")
statements = "돌고래 멸종위기"
print(statements.split())
