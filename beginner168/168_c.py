# 余弦定理から、a**2 = b**2 + c**2 - 2bccosA
# ヨビノリの授業動画で三角関数の理解を深める

# import math
# a,b,h,m = map(int,input().split())
# q = abs((h+m/60)/12-m/60) * 360
# print(math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(q))))


import math

A, B, H, M = map(int, input().split())


'''
時計の角度はいくつか？
長針は６０分で１回展（360度）回るので1分あたりに進む角度は、
360 / 60 = 6

よって、時間が6分だったら 6*6=36度回る

短針は12時間で1回展（360度）まわるので1分辺りに進む角度は
360 / (12*60) = 0.5 度回る
よって時間が6分だったら 6*0.5=3度回る
'''

longAngle  = M * 6
shortAngle = (H * 60 + M) * 0.5
#角度からラジアンを求めて、そのラジアンからcosを求める
Angle      = math.cos(math.radians(abs(longAngle - shortAngle)))

# b**2 = c**2 + a**2 − 2ca *cosB
result = math.sqrt(A**2 + B**2 - 2*A*B*Angle)

print(result)

