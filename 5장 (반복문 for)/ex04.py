# 1~100까지 누적값을 구하는데 누적값이 2000이상이 되면 for 문을 빠져 나오는
# 프로그램을 작성하시오

sum = 0

for i in range(101):
    # 2000이상이면 for 루프를 빠져 나오는 코드
    if sum >= 2000:
        print("마지막으로 더해지는 i의 값 :", i-1)
        break
    else:
        sum += i
print("sum : ", sum)



## 참고(매우 중요함): 중단점을 활용하여 한 단계씩 변수 값이 변화되는 과정을 살펴보면서 디버깅(에러를 잡아나가는 과정) 할 수가 있다.