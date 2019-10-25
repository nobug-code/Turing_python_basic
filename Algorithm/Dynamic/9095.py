#다이나믹 관련 백준 문제

def dynamic():

    temp = [0 for i in range(1000)]
    temp[0] = 0
    temp[1] = 1
    temp[2] = 2
    temp[3] = 4
    for num in total_list:
        for j in range(4, num+1):
            temp[j] = temp[j-3] + temp[j-2] + temp[j-1]
    return temp

total = int(input())
total_list = []

for i in range(total):
    total_list.append(int(input()))

anwser = dynamic()
print(anwser)

for temp in total_list:
    print(anwser[temp])
