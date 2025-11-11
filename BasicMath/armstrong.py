num=123
temp=num
res=0
while(temp>0):
    res+=(temp%10)**3
    temp//=10

if(res==num):print('True')
else:print('False')
