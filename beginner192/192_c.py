n, k = map(int, input().split())
n = [int(x) for x in list(str(n))]

ans = 0
str_kouzyun = ''
str_syouzyun = ''

for i in range(k):

  kouzyun =  sorted(n, reverse=True)
  syouzyun = sorted(n)

  for i in range(len(kouzyun)):
    str_kouzyun += str(kouzyun[i])

  for i in range(len(syouzyun)):
    str_syouzyun += str(syouzyun[i])



  ans = int(str_kouzyun) - int(str_syouzyun)

  n = list(str(ans))
  n = [int(n) for n in n]
  str_kouzyun = ''
  str_syouzyun = ''



print(ans)

