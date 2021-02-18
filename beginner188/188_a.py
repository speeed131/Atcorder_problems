x, y = input().split()

x = int(x)
y = int(y)


if x > y:
    if y + 3 > x:
        print('Yes')
    else:
        print('No')
else:
    if x + 3 > y:
        print('Yes')
    else:
        print('No')