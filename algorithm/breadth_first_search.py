tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12],
        [13, 14],  [], [], [], [], [], [], [], []]

data = [0]

while len(data) > 0:
    #__dataを取り出して、出力する
    pos = data.pop(0) #指定した要素を削除し、要素の値を取得
    print(pos, end=' ')
    #__取得した要素の
    for i in tree[pos]:
        data.append(i)



