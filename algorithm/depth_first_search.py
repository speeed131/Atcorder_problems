tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
        [13, 14], [], [], [], [], [], [], [], []]

def search(num):
    print(num, end= ' ')
    for i in tree[num]:
        search(i)
# search(0)


data = [0]
while len(data) > 0:
    pos = data.pop()
    print(pos, end=' ')
    for i in tree[pos]:
        data.append(i)

