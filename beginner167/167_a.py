S = input() #ここで標準入力
T = input() #ここで標準入力

char_lengths = len(S)

if S == T[0: char_lengths:]:
    print('Yes')
else:
    print('No')

# こっちのほうが早い
    # if S == T[:-1]:
    #     print('Yes')
    # else:
    #     print('No')