#BFS_DFS 관련 백준 문제

import queue
matrix = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
visited =[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
arrow = [[0, 1], [1, 0], [0, -1], [-1, 0]]

''''
[0][0] [0][1] [0][2]
[1][0] [1][1] [1][2]
[2][0] [2][1] [2][2]
'''
q = queue.Queue()

q.put((0, 0, 0))
visited[0][0] = 1

while(q.empty() == False):

    x, y, count = q.get()
    if(x == 3 and y == 5):
        print(count)
        break;
    for i in range(len(arrow)):
        c_x = x + arrow[i][0]
        c_y = y + arrow[i][1]

        if(c_x < 4 and c_x >= 0 and c_y < 6 and c_y >= 0):
            if(matrix[c_x][c_y] == 1 and visited[c_x][c_y] == 0):
                q.put((c_x, c_y, count + 1))
                visited[c_x][c_y] = 1
