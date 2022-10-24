# 일회용 패스워드 생성기를 이용하여서 3개의 패스워드를 생성하여 출력하는
# 프로그램을 만들어보자.
# 패스워드의 길이는 6개의 자리로 한정한다.
# 난수가 발생되는 범위값을 지정을 아래와 같이 한다.
# 난수 발생 문자열 : "0123456789"

import random

def get_Password():
    num_str = "0123456789"
    password = ""
    for i in range(6):
        index = random.randrange(len(num_str))
        password = password + num_str[index]
    return password

print("본인 인증을 위해서 발송한 숫자를 입력하세요 :", get_Password())