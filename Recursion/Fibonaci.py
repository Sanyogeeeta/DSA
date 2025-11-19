def fibonacci_series(num):
    curr=1
    prev=0
    if num==0:
        print(0)
        return
    if num==1:
        print(prev,curr,end=' ')
        return
    
    print(prev,curr,end=' ')   
    for i in range(num-2):
        temp=curr
        curr=prev+curr
        print(curr,end=' ')
        prev=temp

fibonacci_series(5)
        
