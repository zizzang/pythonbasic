# 학생들의 성적을 처리하는 프로그램을 만들기
# 조건 : 사용자로부터 성적을 입력을 받아서 리스트에 저장한다.
# 성적의 평균을 구하고 해당 점수가 80점 이상 성적을 받은 학생의 수를 출력하라.
# 학생수는 상수값으로 STUDENT = 5 를 이용한다.
# 출력결과
# 성적을 입력하시오 : 10
# 성적을 입력하시오 : 20
# 성적을 입력하시오 : 60
# 성적을 입력하시오 : 70
# 성적을 입력하시오 : 80
# 성적 평균은 48.0 입니다.
# 80점 이상 성적을 받은 학생은 1명입니다.


#  내 풀이
def main():
    STUDENT = 5
    score = []
    scoresum = 0
    count = 0

    for i in range(STUDENT):
        score.append(int(input("성적을 입력하시오 : ")))
        scoresum += score[i]
        if score[i] >= 80:
            count += 1
    print("성적 평균은 ", scoresum/len(score), "입니다.")
    print("80점 이상 성적을 받은 학생은", count, "입니다.")

if __name__ == "__main__":
    main()
    
# 강사 풀이

# STUDENT = 5         # 전역 상수 선언
# scores = []         # 학생들의 성적을 저장할 리스트
# score_Sum = 0       # 학생들의 성적 합계를 저장할 변수
# score_aver = 0.0    # 학생들의 성적 평균을 저장할 변수
# cnt_80 = 0          # 80점 이상인 학생수 합계를 저장할 변수

# for i in range(STUDENT):
#     score = int(input("성적을 입력하세요 : "))
#     scores.append(score)        # 학생들의 성적을 list 에 저장함 (append() 이용)
#     score_Sum += score          # 성적 합계
#     if score >= 80:
#         cnt_80 += 1

# score_aver = score_Sum / len(scores)        # 평균을 구함
# print("성적 평균은 ", score_aver, "입니다.")
# print("80점 이상 성적을 받은 학생은", cnt_80, "입니다.")

    