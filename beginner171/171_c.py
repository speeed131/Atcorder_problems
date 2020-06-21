k = int(input()) #ここで標準入力

# 数値→アルファベット
# https://tanuhack.com/num2alpha-alpha2num/
# これを理解しよう
def num2alpha(num):
    if num<=26:
        return chr(64+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num%26)

#１０進数を２６進数に変えれば良い。
# t = 0
# # print(len(a))
# for i in range(k):
#     k = k /26
#     t += 1
#     if k < 26:
#         amari = int(k % 26)
#         break
# print(k)
# print(t)
# print(amari)

print(num2alpha(k).lower())