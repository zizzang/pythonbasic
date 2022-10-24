# 기본적인 파일 입출력 실습
data = []
# 파일의 경로를 지정하고 읽기 모드로 문자셋 UTF-8로 설정해서 해당 파일을
# 열고 메모리에 로딩된 파일의
fp = open("C:\\Temp\\test.txt", mode="r", encoding="UTF=8")
# print(type(fp))
# print(fp)
# readlines() 메서드는 파일의 저장된 내용을 한번에 다 읽는다.
for line in fp.readlines():
    # strip() 메서드는 원래 문자열의 양쪽 공백을 제거하는 역할을 하지만,
    data.append(line.strip())
    # 파일을 읽어들일때는 엔터키 제거를 해준다,
    print(line.strip())     #strip을 써서 양쪽 공백을 없애 줌
# 프로그램에서 리소스를 다 사용했으면 반드시 close()메서드를 호출 하도록 한다.
print("파일에서 읽은 내용입니다.")
print(data)
fp.close()

# 파일에 내용쓰는 방법
# 파일의 모드가 ''w인 경우에는 기존파일의 내용을 덮어써버린다.''
fp = open("C:\\Temp\\test.txt", mode="w", encoding="UTF=8")
fp.write("우리는 파이썬을 공부합니다.")
fp.write("저희도 파이썬을 공부합니다.")
print("쓰기 완료")
fp.close()

# 기존 파일의 내용에 추가를 해준다.
fp = open("C:\\Temp\\test.txt", mode="w", encoding="UTF=8")
fp.write("11.우리는 파이썬을 공부합니다.")
fp.write("22.저희도 파이썬을 공부합니다.")
print("추가 완료")
fp.close()


# CSV 파일 불러오기
import csv
fp = open("C:\\Temp\\sample2.csv", mode="r", encoding="utf=8-ansi")
reader = csv.reader(fp)
for txt in reader:
    print(txt)
# print(reader)
