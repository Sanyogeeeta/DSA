n=5
for i in range(n,0,-1):
    temp=65
    for j in range(i+1):
        print(chr(temp),end='')
        temp+=1
    print()
        