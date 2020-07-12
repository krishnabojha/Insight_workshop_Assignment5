########### Binary search
def binary_search(arr,r,l,x):
    if l>=r:
        mid=r+(l-r)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,r,mid-1,x)
        else:
            return binary_search(arr,mid+1,l,x)
    else:
        return -1
    
str_list=input('Enter numbers of list separated by space : ').split()
arr=[]
for i in str_list:
    arr.append(int(i))
arr.sort()
print('sorted input array : ',arr)
find=int(input('Enter a number you want to search : '))
result = binary_search(arr,0,len(arr)-1, find) 

if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")