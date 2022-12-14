# 파일을 읽어서 리스트에 저장하기
# 파일에서는 데이터를 읽어서 리스트에 저장하는 작업은 아주 많이 등장한다. 기본적인 방법을 알아두자.
# ex)
data = []
f = open("C:\\temp\\data.txt", "r")
for line in f.readlines():       # 파일에 저장된 모든 줄을 읽는다.
    data.append(line.strip())    # 줄바꿈 문자를 삭제한(공백을 없애줌) 후에 리스트에 추가한다.
print(data)

# 정렬하기
a = [3, 2, 1, 5, 4]
a.sort()
print(a)

# 경우에 따라서는 우리가 정렬을 구현해야 하는 경우도 있다.
# 선택 정렬은 가장 이해하기가 쉬운 정렬 방법이다.
# 메모리를 절약하기 위하여 입력 리스트 외에 추가적인 공간을 사용하지 않는 선택 정렬 알고리즘.
# 입력 리스트 이외에는 다른 추가 메모리를 요구하지 않는 정렬 방법을 제자리 정렬(in-place sort) 라고 한다.
# 선택 정렬 알고리즘을 생각해보자.
# 선택정렬 말고도 ''버블정렬, 삽입정렬, 병합정렬, 퀵정렬, 힙정렬''이 존재한다.
