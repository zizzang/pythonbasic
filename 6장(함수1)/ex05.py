# 사용자로부터 정수를 입력받아서 소수를 판별하는 함수 is_prime()을 작성해보자.
# 소수면 True, 소수가 아니면 False 출력 하도록 만든다.
# 소수는 1과 자기자신과 나누어지느 수를 소수라고 한다.
# 그러므로 자기자신 외에 하나라도 나누어 떨어지면 소수가 아니다
# 그렇기 때문에 아래와 같이 코드 작성 가능



def is_prime(x):
    for i in range(2, x):
        temp = True
        if (x % i) == 0:
            temp = False
            break
        else:
            temp = True
    return temp

# 함수 호출
prime = int(input())
print(is_prime(prime))
        
        