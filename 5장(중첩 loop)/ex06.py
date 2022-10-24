# 사용자로부터 전화번호를 입력받다 보면 "-"를 적는 경우가 많다.
# "-"을 합하여 입력 받도록 하고 출력을 할 때는 "-"를 삭제를 한 문자열을 출력하는
# 프로그램을 만드시오.

from curses.ascii import isdigit


# 내 코드

# phnum = input("전화번호(- 포함) : ")
# num = ""
# for i in phnum:
#     if i.isdigit():
#         num += i
# print(num)


# 강사 코드

# phone_num = input("당신의 전화번호를 입력하세요.(-포함) : ")
# new_phone_num = ""

# for ch in phone_num:
#     # 루프문자가  "-"아니라면 참을 반환한다.
#     if ch !="-":
#         new_phone_num += ch
# print("'-'를 제거한 전화번호 : " + new_phone_num)



# 위의 예제에서 전화번호를 잘못(자리수 오입) 입력했을 경우 돌아가서 다시 돌리게 하는 코드 추가

phone_num = input("당신의 전화번호를 입력하세요.(-포함) : ")
new_phone_num = ""

if len(phone_num) != 13:
    for ch in phone_num:
        # 루프문자가  "-"아니라면 참을 반환한다.
        if ch != "-":
            new_phone_num += ch
    print("'-'를 제거한 전화번호 : " + new_phone_num)
else:
    print("잘못된 값을 입력 하였습니다. 다시 입력하시오")



