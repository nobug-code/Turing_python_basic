stack = []
SIZE = 100
position = -1

def push(data,stack,SIZE,position):
    #Overflow function
    if(position == SIZE):
        print("overflow")
    else :
        stack.append(data)
        position = position + 1
    return stack,position

def pop(stack,position):

    #underflow
    if(position == -1):
        print("underflow")
        return "error",position
    temp = stack[position]
    del stack[position]
    position = position - 1
    return temp,position

while(True):
    choice = int(input('input the choice (1 is push , else is pop) : '))
    if(choice == 1):
        data = int(input('input the daat value : '))
        stack,position = push(data,stack,SIZE,position)
    else:
        data,position = pop(stack,position)

    print('stack', stack)
    print('data', data)
    print('position', position)