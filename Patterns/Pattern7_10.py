n=5
for i in range(n+1):
    for j in range(n-i):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    for j in range(n-i):
        print(' ',end='')
    print()

n=5
for i in range(n,-1,-1):
    for j in range(n-i):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    for j in range(n-i):
        print(' ',end='')
    print()

for i in range(1,n+1):
    print('*'*i)
for j in range(n-1,-1):
    print('*'*j)



