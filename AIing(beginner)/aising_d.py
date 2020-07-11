N = int(input())
X = list(input())
result = ''

for i in range(N):
    if X[i] == '0':
        X[i] = '1' 
    elif X[i] == '1':
        X[i] = '0'

    "".join(X)
    count = X.count('1')

    for j in range(100000):
        decimal = int(int(X) ,2) 
        if decimal % count == 1:
            result += '1'
        else:
            result += '0'

        decimal = decimal // count
        count = bin(decimal).count('1')

    print(int(result, 2))
