n = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]



m = n-1

yakusu = make_divisors(m)

yakusu_count = len(yakusu)

k = 1

for i in range(1, yakusu_count + 1):
    k *= i


print(k+1)
