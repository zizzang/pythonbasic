# 섭씨 온도를 사용자로 부터 입력을 받고
# 화씨 온도로 변환하여 반환하는 함수 FtoC()
 # main 함수를 추가해서 순서를 맞춰 줬음 (이런게 있다 정도만 알고 있으면 됨)
 
def main():
    print(round(FtoC(temp_f),2))

temp_f = float(input())

# 함수 호출

# 함수 선언 및 구현
def FtoC(temp_f):
    temp_c = (5.0 * (temp_f - 32.0))/9.0
    return temp_c

main()