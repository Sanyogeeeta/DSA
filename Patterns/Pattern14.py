n=5
temp=65
for i in range(n):
    for j in range(i+1):
        print(chr(temp),end='')
        temp+=1
    print()
        