
n=4
for i in range(1,2*n):
    temp=n
    for j in range(1,2*n):
        if(i==1 or j==1 or j==(2*n-1) or i==(2*n-1)):
            print(n,end='')
        elif((j-i)<=0):
            temp-=1
            print(temp,end='')
        elif((j-i)>=temp or (i-j)>=temp):
            print(temp,end='')
            temp+=1
        else:
            print(temp,end='')
    print()