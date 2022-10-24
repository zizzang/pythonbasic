# 매개변수와 지역변수의 관계 (매개변수 = 지역변수)
# 함수가 외부로부터 값을 전달 받는데 사용하는 매개변수도 일종의 지역변수이다.

def sub(mylist):
    # 리스트가 함수로 전달된다.
    mylist = [1,2,3,4]  # 새로운 리스트가 매개변수로 할당된다.
    # mylist += [1,2]
    print("함수 내부에서의  mylist: ", mylist)
    return # mylist

# 여기서 sub() 함수를 호출한다.
mylist = [10,20,30,40]
sub(mylist)
print("함수 외부에서의 mylist: ", mylist)