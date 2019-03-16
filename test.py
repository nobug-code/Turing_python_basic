a = []

for i in range(8):

    a.append(int(input()))

#버블 정렬

b = [1,2,3,4,5,6,7,8]

for i in range(len(a)):

    for j in range(len(a) -i - 1):

        if(a[j] < a[j + 1]):

            a[j],a[j+1] = a[j+1],a[j]
            b[j],b[j+1] = b[j +1],b[j]


for i in range(5):

    for j in range(5 - i - 1):

        if(b[j] > b[j + 1]):

            b[j],b[j+1] = b[j+1],b[j]


print("%d %d %d %d %d"%(b[0],b[1],b[2],b[3],b[4]))