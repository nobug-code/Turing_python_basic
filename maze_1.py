from collections import deque
deq = deque()
# Add element to the end
deq.append([1,2])
deq.append([3,2])
# Pop element from the start
print(deq.popleft())

# 어떻게 저장 할꺼야?
'''
0 0 0 
0 0 0 
0 0 0
'''

'''
이중 리스트로 저장
'''
# arr = []
# for i in range(3):
#     arr.append(list(map(int, input().split())))
# print(arr)

'''
위에 리스트가 

1 2 3
6 5 4
7 8 9 
가 되도록 만들어 주세요
'''

arr = []
for i in range(3):
    arr.append(list(map(int, input().split())))

deq = deque()
# Add element to the end
deq.append([0,0])
count = 1

# x,y list
arrow_list = [[0,1],[0,-1], [1,0]]

while True:

    if len(deq) == 0:
        print("end")
        break

    x, y = deq.popleft()
    arr[x][y] = count

    print(x, y)
    print(arr)

    for a_x, a_y in arrow_list:

        later_x , later_y = x + a_x, y + a_y
        if 0 <= later_x < len(arr) and 0 <= later_y < len(arr):

            if arr[later_x][later_y] == 0:
                    count += 1
                    deq.append([later_x, later_y])
                    break
print(arr)

# 이걸이용해서 미로 찾기 해보기
'''
1 0 0 
1 0 0 
1 1 1
1만 지나 갈 수 있는 길이다. 
'''