n=5
for i in range(n,0,-1):
    for j in range(n):
        if(j<i):print('*',end='')
        else:print(' ',end='')
    for j in range(n-1,-1,-1):
        if(j<i):print('*',end='')
        else:print(' ',end='')
    print()
for i in range(n):
    for j in range(n):
        if(j<=i):print('*',end='')
        else:print(' ',end='')
    for j in range(n-1,-1,-1):
        if(j<=i):print('*',end='')
        else:print(' ',end='')
    print()
