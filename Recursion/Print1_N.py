
def PrintNum(num,n):
    if(num==n+1):
        return
    print(num)
    return PrintNum(num+1,n)

num=1
n=5
PrintNum(num,n)