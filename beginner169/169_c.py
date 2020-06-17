# A, B = input().split()
# A = float(A)
# B = float(B)



# output = A * B
# print(int(output))

##浮動小数点型の誤差の証明。答えは0.9999999999・・・になる
# a = 0.1
# b = a + a + a + a + a + a + a + a + a + a
# print(b)

from math import floor
# decimalモジュールからDecimal関数を読み込む
from decimal import Decimal
a, b = input().split()
a = int(a)
b = Decimal(b)
print(floor(a * b))