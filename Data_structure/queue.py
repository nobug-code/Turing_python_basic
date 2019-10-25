def enqueue(data):

    queue_list.append(data)

def dequeue():

    if(len(queue_list) == 0):
        print("empty list")
    queue_list.pop(0)


queue_list = []
