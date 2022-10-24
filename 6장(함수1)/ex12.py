# 사용자로부터 10진수를 입력받아서 2진수 문자열로 변환하여 반환하는
# 함수 decTobin(num) 를 작성하고 테스트 해보시오.

def decTobin(num):
    binary = ""
    while num != 0: 
        value = num % 2
        if value == 0:
            binary = "0" + binary
        elif value == 1:
            binary = "1" + binary
        num = num // 2
        print("num : ", num)
    return binary

decNum = int(input())
print(decTobin(decNum))


# 파이썬에서 제공하는 진법 변환 함수

print(bin(10)) # 2진수로 변환하는 내장함수
print(oct(10)) # 8진수로 변환하는 내장함수
print(hex(10)) # 16진수로 변환하는 내장함수


# 2진수의 값을 10진수로 변환하는 방법
print(int("0b1010", 2))
print(int("0o12", 8))
print(int("0xa", 16))
