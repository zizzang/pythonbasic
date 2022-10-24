# 최소값과 최대값 구하기
# min(), max() 를 이용하여 숫자들이 들어 있는 리트트에서 최소, 최대 값을 구할 수 있다.
# 하지만 리스트에 숫자가 아닌 다른 종류의 데이터 타입이 들어 있다면 일반적인 알고리즘을 알고 있어야한다.
# 리스트에 저징된 값들의 최대값이나 최소값을 어떻게 계산하는지를 생각해보자. 이것은 실제 프로그램이에서도
# 상당히 많이 등장하는 문제이므로 정확하게 알고 있어야 한다.

# list 내 최소값 구하기 
# ex)
# s = [-10, -50, 100, 50, -7.2]
# min = s[0]
# for i in range(1, len(s)):
#     if min > s[i]:
#         min = s[i]
# print("최소값 : ", min)

# 최소값과 최대값 구하기

# list 내 최소 문자열 구하기
# ex)
words = ["cat", "moust", "tiger", "lion"]
shortest = words[0]
for i in range(1, len(words)):
    if len(words[i]) < len(shortest):
        shortest = words[i]
print("가장 짧은 단어는", shortest)