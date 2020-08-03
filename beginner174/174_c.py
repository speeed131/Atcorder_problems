k = int(input())
# print(k[0:-1:])

# first = int(k[-1]) * 2 

# second = int(k[0:-1:]) - first 


a = 7
ans = False




for i in range(1, 1000000):
    if k % 2 == 0:
        print(-1)
        break
    if int(a) % k == 0:
        print(i)
        ans = True
        break
    a = str(a) + '7'
        

