N = str(input()) #ここで標準入力

car = ''
if N[-1] == '3':
    car = 'bon'
elif N[-1] == '0' or N[-1] == '1' or N[-1] == '6' or N[-1] == '8':
    car = 'pon'
else:
    car = 'hon'



print(car)