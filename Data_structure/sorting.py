matrix = []

import random

LEN = 10

for i in range(LEN):
    temp = random.randrange(1, 50)
    matrix.append(temp)

for i in range(1, LEN):

    temp = matrix[i]
    j = i - 1
    while(temp < matrix[j] and j >= 0 ):
        matrix[j+1] = matrix[j]
        j -= 1
    matrix[j+1] = temp

print(matrix)