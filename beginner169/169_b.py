#intの場合
N = int(input()) #ここで標準入力

A = list(map(int, input().split()))

# multiple = 1
# for i in range(N):
#     multiple *= A[i]



# if multiple <= 10 ** 18 :
#     print(multiple)
# else:
#     print(-1)

def main():
    if 0 in A:
        print(0)
        return

    output = 1
    for a in A:
        output *= a

        if output > (10 ** 18):
            print(-1)
            return

    print(output)

main()
