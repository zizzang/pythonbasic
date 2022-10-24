#  더블 루프를 이용하여 아래와 같이 출력 하는 프로그램을 작성하시오.
#  출력결과

#     *
#    ***
#   *****
# *********
# 더블 루프 사용(1)
for i in range(1, 6):
    # 공백을 찍는 내부 루프
    for y in range(5-i):
        print(" ", end="")
    # 별표를 찎는 내부 루프
    for j in range(1, i*2):
        print("*", end="")
    # 줄 바꿈
    print("")
    

# format 함수 사용(2)    
print("-----------------------------------")
for i in range(1, 11, 2):
    print("{:^10}".format("*" * i))     # 가운데 정렬은 '^' 사용
    
    
    


# 출력결과
#     *
#    ***
#   *****
# *********
# *********
#   *****
#    ***
#     *

print("-----------------------------------")
# 위의 삼각형
for i in range(1, 11, 2):
    print("{:^10}".format("*" * i))

# 아래 절반의 역삼각형
for i in range(5):
    for y in range(i):
        print(" ", end="")
    for j in range(10, (i*2)+1, -1):
        print("*", end="")
    print("")