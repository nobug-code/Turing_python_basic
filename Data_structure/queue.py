def enqueue(num):

    if(len(queue) > max):
        print("overlow")
        return
    else:
        queue.append(num)


def dequeue():

    if(len(queue) == 0):
        print("underflow")
        return
    else:
        del queue[0]
        return

max = 5
queue = []

while(True):

    input_str = input()
    if(input_str == "in"):
        num = int(input("숫자를 입력해 주세요:"))
        enqueue(num)
    elif(input_str == "de"):
        dequeue()