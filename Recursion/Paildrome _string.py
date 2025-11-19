str='AbA'

def is_palindrome(str):
    n=len(str)
    temp=[]
    for i in range(n):
        temp.append(str[n-i-1])

    if(temp==str):
        return print("True")
    else:
        return print("False")
is_palindrome(str)