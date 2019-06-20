a = int(input())

money = [500,100,50,10]

count = 0

while(a >= money[0]):
    a = a - money[0]
    count = count + 1
while(a >= money[1]):
    a = a - money[1]
    count = count + 1
while(a >= money[2]):
    a = a - money[2]
    count = count + 1
while(a >= money[3]):
    a = a - money[3]
    count = count + 1

print("output is",count)

