#  값으로 호출, 참조로 호출의 차이점

# 정수형
# def func(x):
#     print("x = ", x, "address", id(x))
#     x += 15
#     print("x = ", x, "address", id(x))

# y = 10      # 정수형(변경 불가능한 객체)
# print("y = ", y, "address", id(y))
# func(y)     # 함수 호출(값에 의한 호출)
# print("y = ", y, "address", id(y))


# 리스트형 
def func_li(x):
    print("x = ", x, "address", id(x))
    x.append("하세요")
    print("x = ", x, "address", id(x))

y = [10, 20, 30]     # 정수형(변경 불가능한 객체)
print("y = ", y, "address", id(y))
func_li(y)     # 함수 호출(값에 의한 호출)
print("y = ", y, "address", id(y))