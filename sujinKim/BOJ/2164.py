#N장의 카드 -> 차례로 1부터 N까지의 번호가 붙어 있어서 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 높여 있다. 
# 제일 위에 있는 카드를 바닥에 버리고, 그 다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다. 
# N = 4인 경우 카드는 제일 위에서부터 1234의 순서로 놓여있다. 
# 1을 버리면 234가 남고, 여기서 2를 제일 아래로 옮기면 342가 됨. 

from collections import deque ##

N = int(input())  #N장의 카드가 있으면 
cards = deque(range(1,N+1))  ##카드담을곳
while len(cards) > 1: ##카드 한장 남을떄까지
    cards.popleft() ##맨 위 카드 버리겠음

    if cards:  ##만약 카드가 
        top_card = cards.popleft()  ##맨위 한장 버린걸 top_card에 저장했다가
        cards.append(top_card)  ##cards에 추가한다. 

print(cards[0])
# arr = []
# for n in range(1,N+1): #1번부터 N번카드까지 순서대로 있음 그걸 꺼내겠음 위부터
    # arr.append(n) #하나씩 꺼내 넣어서
    # arr.sort() #정렬하겠음

    # if n % 2 != 0 :  #보아하니 홀수만 버려지는듯
    #     arr.pop(n)
    # elif n %2 == 0 :#짝수면 
    #     arr.append(pop(n)) #그걸 빼가지고 뒤에 넣는다. 

    # if len(arr) == 1:
    #     print(n)

