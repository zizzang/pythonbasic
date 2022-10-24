# 리스트 복사하기
# 깊은 복사(deep copy) : 주소값을 공유하는 얕은 복사가 아니라 새로운 리스트 객체를
# 생성해서 새로운 주소값이 할당이 되어 원본 리스트 객체에는 전혀 영향을 끼치지 아니한다.

# 첫 번째 방법 : list()메서드를 이용하는 방법
scores = [10, 20, 30, 40, 50]
refer = list(scores)
print("score")


# 두 번쨰 방법 : copy 모듈에 있는 deepcopy(), copy()를 이용하는 방법
import copy
scores_copy = [10, 20, 30, 40, 50, -10]
refer_copy = copy.deepcopy(scores)
refer[0] = 100
refer.append(-500)
refer.insert(2, -123)
print(id(scores_copy)) # 복사해서 새로운 객체로 생성됨 = ID 주소 값 다름
print(id(refer)) # 복사해서 새로운 객체로 생성됨 = ID 주소 값 다름

# 세 번째 방법 : [:] 인덱스를 이용하여 깊은 복사를 하는 방법
scores_index = [10, 20, 30, 40, 50, -10]
refer_index = scores_index[:]
refer_index[0] = 100
refer_index.append(-500)
refer_index.insert(2, -123)
print(id(scores_index)) # 복사해서 새로운 객체로 생성됨 = ID 주소 값 다름
print(id(refer_index)) # 복사해서 새로운 객체로 생성됨 = ID 주소 값 다름

