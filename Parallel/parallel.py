import multiprocessing
import time

#parallel
start_time = time.time()

def count(name):
    total = 0
    for i in range(1,50000001):
        total += i

num_list = ['a1','a2','a3','a4']

'''
for num in num_list:
    count(num)
'''

if __name__ == "__main__":

    pool = multiprocessing.Pool(processes=6)
    pool.map(count,num_list)
    pool.close()
    pool.join()

print("--- %s seconds ---"%(time.time() - start_time))

#클래스의 유지보수를 어떻게 할 것인가

