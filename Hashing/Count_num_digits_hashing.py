arr=[1,23,11,1,23,1]
count_digits={}
for num in arr:
    count_digits[num]=count_digits.get(num,0)+1
        
print(count_digits)