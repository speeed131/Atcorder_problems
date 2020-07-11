#__１０進数を２進数に__
n = int(input())
result = ''

while n > 0:
    result = str(n % 2) + result
    n     //= 2

print(result)

#___１０進数をn進数に 関数で定義
def decimal_to_n(decimal, n):
    result = ''

    while decimal > 0:
        result    = str(decimal % n) + result
        decimal //= n

    return result

print(decimal_to_n(100, 16))


#__２進数を１０進数に

n = '1011'
result = 0
for i in range(len(n)):
    result += int(n[i]) * (2 ** (len(n) - i - 1))
print(result)

