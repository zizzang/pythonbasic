# 조건문 if 구문만 사용
score = 99
# 몇 십개의 if구문이 존재 하더라도, CPU는 모든 if 문을 참조한다.
# 그러므로 애플리케이션 프로그램의 성능은 떨어질 수 밖에 없다.

if score >= 90:
    print("점수가 90점이상입니다. 학점은 A등급입니다.")

if score >= 80:
    print("점수가 80점 이상입니다. 학점은 B등급입니다.")

if score >= 70:
    print("점수가 70점 이상입니다. 학점은 C등급입니다.")

if score >= 60:
    print("점수가 60점 이상입니다. 학점은 D등급입니다.")