# 탐색하기
# 탐색(search)은 컴퓨터가 가장 많이 하는 작업 중의 하나이다.
# 탐색은 많은 시간이 요구되는 작업이므로 효율적으로 수행하는 것은 매우 중요하다.
# 탐색의 대상이 되는 데이터는 보통 리스트에 저장이되어 있다고 가정한다.
# 탐색이란 리스트에서 특정한 값을 찾는 것이다.
# 리스트에서는 앞서 살벼보았던 index() 메소드를 사용할 수 있따.
# index()는 리스트에서 항목을 찾아서 항목의 인덱스를 반환한다.

# 가장 간단한 알고리즘인 ''순차 탐색''
# 순차탐색은 탐색 방법 중에서 가장 간단하고 직접적인 탐색 방법이다.
# 순차 탐색 ex)
def linear_Search(alist, kye):
    for i in range(len(aList)):
        if key == aList[i]:
            return i
    return -1

numbers = [10,20,30,40,50,60,70,80,90]
position = linear_Search(numbers,80)

if position != -1:
    print("탐색 성공 위치 = ", position)
else:
    print("탐색 실패")