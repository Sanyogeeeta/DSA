n=5
for i in range(n):
    for j in range(n-1,-1,-1):
        temp=65+j
        if(j<=i):print(chr(temp),end='')
        else:print(' ',end='')
    for j in range(1,n):
        temp=65+j
        if(j<=i):print(chr(temp),end='')
        else:print(' ',end='')
    print()