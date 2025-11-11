num=6
is_prime=1
for i in range(2,num//2+1):
    if(num%i==0):
        is_prime=0

if is_prime:print('True')
else:print('False')
