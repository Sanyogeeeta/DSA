n=5
for i in range(1,n+1):
    temp=65+n-i
    for j in range(1,i+1):
        print(chr(temp),end='')
        temp+=1
    print()
