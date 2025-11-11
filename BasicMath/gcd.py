def gcd(num1,num2):
    if(num1<num2):
        num1,num2=num2,num1
        # return gcd(num2,num1%num2)
    while(num2!=0):
        num1,num2=num2,num1%num2
        
    return num1
    
print(gcd(4,18))
    