def Reverse(num):
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev

num=12129
temp=Reverse(num)
if temp==num:print('True')
else:print('False')
