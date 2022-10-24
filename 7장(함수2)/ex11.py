# 여러 개의 값을 반호나하는 함수 실습
# 타 프로그래밍 언어에서는 함수가 항상 하나의 값만을 반환하하거나 반환값이
# 없다. 파이썬에서는 튜플을 이용하여 어러 개의 값을 반환할 수가 있다.
# 튜플(tuple)은 몇 가지만 제외하고 리스트와 거의 비슷한 자료구조 형태이다.
# - 리스트는 []으로 값을 둘러싸지만, 튜플은 ()로 값을 둘러싸는 형태이다.
# - 리스트는 변경가능한(mutable) 객체(생성, 삭제, 수정, 추가)이지만
# - 튜플은 한 번 값을 만들면 그 변경을 변경할 수 없는(immutable) 객체이다.

# 파이썬에서는 튜플의 형태로 여러 개의 값을 리턴을 하긴 하지만,
# 함수는 한 가지의 값을 리턴해준다라는 그 정설에는 부합하다.
# 그 이유는 튜플이라는 형태로 1개를 넘기기 때문이다.
def tuple_return():
    return 1, "안녕", 5

a, b, c = tuple_return()
tuple_variable = tuple_return()
# tuple_variable += 10 > 이와 같은 추가가 안됨 변경불가 객체이기 때문에
print(a, b, c)
print(tuple_variable)
print(type(tuple_variable))


li = list(tuple_variable) # 이런식으로 리스트로는 변경 가능함
li.append("반갑습니다.") # append로 넣어주면 문자열이 그대로 삽입됨
print(li)