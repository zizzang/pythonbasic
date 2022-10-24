# 일반적인 리스트 연산들 실습
# 최소값 최대값을 구하는 알고리즘

# 아래 코드는 앞서 이미 배웠다. 내장함수를 이용하여 최소값 최대값을 구하는코드이다.
num = [1,5,-9,100]
print("최소값 : ", min(num))
print("최대값 : ", max(num))

# 최대값과 최소값을 구하는 알고리즘은 상당히 중요한 개념이므로 아래의 코드를 구성해보자
prices = [1000,3000,500,10000,20000,700]
# 먼저 ㅔprices[]에 있는  0번째 인덱스 값을 변수에 저장을 한다.
lowPrice = prices[0]
# 이후, 루푸를 돌면서 조건식으로 값이 작으면 해당하는 값을 lowPrice 변수에 재저장
for i in range(1, len(prices)):
    if prices[i] < lowPrice:        # 참이다라는 것은 price[i]가 lowPrice보다 작다라는 의미
        lowPrice = prices[i]
print("가장 싼 가격 : ", lowPrice)

# 문자열에서 가장 짧은 문자열을 구하는 알고리즘 코드
words = ["dog", "cat", "horse", "lion", "tiger", "elephant", "bi"]
# 문자열 리스트에서 min()는 제일 첫 글자가 아스키코드 중에서 가장 작은 단어를
# 반환 해준다.
# print("가장 짧은 단어 : ", min(words))

# 문자열에서 가장 짧은 문자열을 구하는 알고리즘 코드
shortest_word = words[0]
list_word = []
for i in range(1, len(words)):
    if len(words[i]) <= len(shortest_word):
        if len(words[i]) < len(shortest_word):
            list_word.clear()
            list_word.append(words[i])
        else:
            list_word.append(shortest_word)
            shortest_word = words[i]
            list_word.append(shortest_word)

print("가장 짧은 단어이거나 같은 단어들 : ", list_word)

for i in range(len(list_word)):
    print("가장 짧은 단어 : ", list_word)