####### Quick sort
def partition(arr,low,high): 
    i = ( low-1 )   
    for j in range(low , high): 
        if   arr[j] <= arr[high]: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
        
        pi = partition(arr,low,high) 
 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
input_list=input('Enter numbers of list separated by space : ').split()
arr=[]
for num in input_list:
    arr.append(int(num))
n=len(arr)-1
quickSort(arr,0,n) 
print('Sorted list : ',arr)