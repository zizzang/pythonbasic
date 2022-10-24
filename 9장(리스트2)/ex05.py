# 연락처 관리 프로그램 만들기
# 출력결과
# ------------------------------
# 1. 친구 리스트 출력
# 2. 친구 추가
# 3. 친구 삭제
# 4. 이름 변경
# 9. 종료
# 메뉴를 선택하시오 : 2
# 이름을 입력하시오 : 가나다
# ------------------------------
# 1. 친구 리스트 출력
# 2. 친구 추가
# 3. 친구 삭제
# 4. 이름 변경
# 9. 종료
# 메뉴를 선택하시오 : 1
# ['홍길동']
# ------------------------------

# 출력 문구를 나타내는 함수
def menu_print():
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")

# 내 풀이
# def phone_num():
#     f_list = []
#     y = ""
#     x = 0
#     while True:
#         menu_print()
#         x = int(input("메뉴를 입력하시오 : "))
#         if x == 1:
#             print("친구 목록입니다. ", f_list)
#         elif x == 2:
#             f_list.append(input("추가 할 친구 이름을 입력하시오 : "))
#         elif x == 3:
#             print(f_list)
#             y = input("친구 목록 입니다. 삭제 하실 친구 이름을 입력하세요. : ")
#             if y not in f_list:
#                 print("제대로된 이름을 입력하세요.")
#             elif y in f_list:
#                 f_list.remove(y)
#                 print("삭제되었습니다.")
#         elif x == 4:
#             print("친구 목록입니다. ",f_list)
#             z1 = input("변경할 친구 이름 : ")
#             if z1 in f_list:
#                 z2 = input("새로운 이름 : ")
#                 index = f_list.index(z1)
#                 f_list[index] = z2
#             else:
#                 print("해당하는 이름이 없습니다.")
#         elif x == 9:
#             break
# if __name__ == "__main__":
#     phone_num()


menu_choice = 0     # 메뉴 번호를 저장
friends = []        # 친구 목록을 저장할 리스트

while True:
    menu_print()
    menu_choice = int(input("메뉴를 선택하시오 : "))
    
    # 무한 루프 빠져나가는 코드
    if menu_choice == 9:
        print("프로그램을 종료합니다.")
        break 
    elif menu_choice == 1:
        print("친구 리스트 입니다.")
        print(friends)
    elif menu_choice == 2:
        name = input("이름을 입력하시오 : ")
        friends.append(name)
    elif menu_choice == 3:
        del_name = input("삭제하고 싶은 이름을 입력하세요 : ")
        if del_name in friends:     # 리스트에 삭제하고 싶은 이름이 있다면 ....
            friends.remove(del_name)
            print(del_name, "님이 삭제되었습니다.")
        else:
            print(del_name, "님이 존재하지 않습니다.")
    elif menu_choice == 4:
        old_name = input("변경하고 싶은 이름을 입력하세요")
        if old_name in friends:
            index = friends.index(old_name)
            new_name = input("새로운 이름을 입력하세요 : ")
            friends[index] = new_name
        else:
            print(old_name, "님이 존재하지 않습니다.")