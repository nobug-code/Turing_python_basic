import time
'''
def test(n):

    #종료 조건
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return test(n-1) + test(n-2)

start_time = time.time()
print(test(100))
end_time = time.time() - start_time
print(end_time)
    #반환값
'''
start_time = time.time()

a = 100
matrix = []
for i in range(a+1):
    matrix.append(0)

matrix[0] = 0
matrix[1] = 1

for i in range(2, a+1):
    matrix[i] = matrix[i-1] + matrix[i-2]
print(matrix[100])
end_time = time.time() - start_time
print(end_time)
