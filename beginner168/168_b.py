# ○
K = int(input()) 
S = str(input())

deffirence = len(S) - K

if deffirence >  0:
    print(S[0: K:] + '...')
else:
    print(S)

