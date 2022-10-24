# 더하기 함수
def add(x, y):
    return (x + y)

# 빼기 함수
def substract(x, y):
    return (x - y)

# 곱하기 함수
def multiply(x, y):
    return (x * y)

# 나누기함수
def divide(x, y):
    return round((x / y),2)

# 연산자에 의해서 분기를 시킨다.
temp = "y"
# 계산기는 끄기전에는 계속 돌아간다.
while True:
    if temp == "n":
        break
    elif temp == "y":
        n1 = float(input("첫 번째 수 입력 : "))
        n2 = float(input("두 번째 수 입력 : "))
        op = input("원하는 연산을 입력 (+, -, *, /) : ")
        if op == "+":
            print(add(n1, n2))
        elif op == "-":
            print(substract(n1, n2))
        elif op == "*":
            print(multiply(n1, n2))
        elif op == "/":
            print(divide(n1, n2))
        else:
            print("잘못된 연산자 입니다.")
        temp = input("계산을 계속 하시겠습니까 ?(y or n) : ")
    else:
        print("제대로 된 종료문자를 입력해주세요.")
