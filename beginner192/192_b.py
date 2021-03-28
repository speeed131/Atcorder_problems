x = input()

yominikui = True

for i in range(len(x)):
  if i % 2 == 0:
    if x[i].isupper():
      yominikui = False
  else:
    if x[i].islower():
      yominikui = False

if yominikui:
  print('Yes')
else:
  print('No')