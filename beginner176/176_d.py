import numpy as np
h, w = map(int, input().split())
posx, posy = map(int, input().split())
goalx, goaly = map(int, input().split())
a = [list(input()) for i in range(h)]


a[posx -1][posy- 1] = '0'
a[goalx -1][goaly -1] = '1'

print(a)

position = [[1, 1, 0]]

    if a[x][y] == 1:
        print(depth)
        break


# meiro = [
#  for i in expression_list:
#      pass
# ]



