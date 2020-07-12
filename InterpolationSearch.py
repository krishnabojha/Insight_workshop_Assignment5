########### Interpolation search
def interpolationSearch(arr,high,x):
    low=0
    
    while(low<=high and x>=arr[low] and x<=arr[high]):
        if low==high:
            if arr[low]==x:
                return low
            return False

        position=low + int(((float(high - low) /( arr[high] - arr[low])) * ( x - arr[low])))

        if arr[position]==x:
            return position
        
        if arr[position]<x:
            low=position+1
            
        else:
            high=position-1
    return False
    
str_list=input('Enter numbers of list separated by space : ').split()
arr=[]
for i in str_list:
    arr.append(int(i))
arr.sort()
print('sorted input array : ',arr)
find=int(input('Enter a number you want to search : '))
result = interpolationSearch(arr,len(arr)-1,find) 

if result != -1: 
    print ("{} is present at index {}".format(find,result)) 
else: 
    print ("Element is not present in array")