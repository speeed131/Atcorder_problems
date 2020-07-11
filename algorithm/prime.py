import math

def is_prime(num):
    if num < 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)): #ここで＋１する
        if num % i == 0:
            return False
    return True

# print(is_prime(131))

# for i in range(100):
#     if is_prime(i):
#         print(i)


def get_prime(n):
    if n <= 1:
        return []
    prime = [2]
    limit = int(math.sqrt(n))

    # 奇数のリストを作成
    data = [i + 1 for i in range(2, n, 2)]
    print(data)
    while limit > data[0]:
        prime.append(data[0])
        # 割り切れない数だけを取り出す
        data = [j for j in data if j % data[0] != 0]

    # return prime + data

# print(get_prime(200))

get_prime(100)