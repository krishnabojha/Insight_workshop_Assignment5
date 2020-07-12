########## linear search
def linearsearch(arr,x):
    for i in range(len(arr)-1):
        if(arr[i]==x):
            return True,i
    return False,0
str_list=input('Enter numbers of the list separated by space : ').split()
find=int(input('Enter number you want to search : '))
arr=[]
for num in str_list:
    arr.append(int(num))

response,index=linearsearch(arr,find)
if response==True:
    print('{} is in index {}'.format(find,index))
else:
    print('The number you search is not present.')