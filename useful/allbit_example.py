# https://note.nkmk.me/python-bin-oct-hex-int-format/
# bin()１０進数を２進数に直す
i = 5
bin(i) # 0b101
bin(i >> 2) # 0b1
# print((i >> 2)& i) # 5 を 2 回右にシフトしたものと 1 の論理積は 1 (=True)




# みかん（100円）りんご（200円）ぶどう（300円）がそれぞれ1つずつ果物屋さんにありました。財布の中には300円ありますが、考え得るすべての買い物パターンを列挙しなさい。
money = 300
item = (("みかん", 100), ("りんご", 200), ("ぶどう", 300))
n = len(item)
for i in range(2 ** n):
    # ここで必要なチェックを行う
    # print(bin(i))
    # で２進数も見てみると良い
    total = 0
    bag = []
    # print("pattern {}:".format(i), end="")
    for j in range(n): # ｊは0,1,2の繰り返し
        if((i >> j) & 1): #iを２進数表記したものを順に右にシフトさせ最下位bitのチェックを行う
            bag.append(item[j][0]) # フラグが立っていたら bagに果物を詰める
            total += item[j][1]
    if(total <= money):
        print(total, bag)

        

