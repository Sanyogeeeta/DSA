num=4

def printName(name,num,count):
    if(count==num):
        return
    print(name)
    printName(name,num,count+1)

count=0
printName('Adi',4,0)