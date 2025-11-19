arr=[1,2,3,4,5,8,6,6,0]
def rev_array(arr,count):
    length=len(arr)
    arr[count],arr[length-count-1]=arr[length-count-1],arr[count]
    if count==length//2-1:
        #arr[count],arr[length-count-1]=arr[length-count-1],arr[count]
        return arr
    else:
        return rev_array(arr,count+1)
        
print(rev_array(arr,0))


        
