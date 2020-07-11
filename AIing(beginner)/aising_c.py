import math
N = int(input())


# if a * a + b * b + c * c + ab + bc + ac == i:
    
count = 0

for i in range(1, N + 1):
    if i < 6:
        print(0)
        continue
    sqrt = int(math.sqrt(i))
    for x in range(1, sqrt + 1):
        if x**2 > i:
            break
        for y in range(1, sqrt + 1):
            if x * x + y*y + x*y > i:
                break
            for z in range(1, sqrt + 1):
                 if (x + y + z) ** 2 -x*y -y*z -x*z == i:
                     count += 1
    print(count)
    count = 0