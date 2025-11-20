arr=[23,11,1,23,1]
count_digits={}
for num in arr:
    count_digits[num]=count_digits.get(num,0)+1
        
max_value=max(count_digits.values())
for key,value in count_digits.items():
    if value==max_value:
        print(key)