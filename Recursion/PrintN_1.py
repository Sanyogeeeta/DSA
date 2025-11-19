
def PrintNum(num,n):
    if(num==0):
        return
    print(num)
    return PrintNum(num-1,n)

num=5
n=5
PrintNum(num,n)
