# 소수를 2부터 계속 더할 때, 2000까지 루푸를 돌리고, 소수와 합계
# 그리고 마지막으로 더해지는 소수는 얼마인지 출력하는 프로그램을 작성해보자
# 단, 더블루프와 조건식을 사용해야 함

start_num = 0   # 사용 변수 초기화
num = 0         # 사용 변수 초기화
sum = 0         # 사용 변수 초기화
lastData = 0    # 사용 변수 초기화

# 어렵다 ...
for num in range(2, 2001):
    for start_num in range(2, num+1):
        # 배수이거나 소수인지를 걸러내는 조건식
        if num % start_num == 0:
            break
    # 아래 조건이 참이다라는 것은 자기자신으로 나눠서 나머지가 0이 나왔다는 #### <<< 이게 중요
    # 것은 바로 소수를 의미하므로 아래 코드가 돌아간다.
    if num == start_num:
        print("소수 : ", + start_num)
        sum += start_num
        print("합계 : ", sum)
        lastData = start_num
        print("마지막 소수의 값 : ", lastData)
        print("======================================")
        