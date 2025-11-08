n=5
for i in range(n):
    print('*'*n)

for i in range(n):
    print('*'*i)

for _ in range(1,n+1):
    for i in range(1,_+1):
        print(i,end='')
    print()

for i in range(1,n+1):
    print(str(i)*i)

for i in range(n+1):
    print('*'*(n-i))

for i in range(n+1,0,-1):
    for j in range(1,i):
        print(j,end='')
    print()









    9