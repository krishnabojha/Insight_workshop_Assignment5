##### mergeSort
def mergeSort(num_list):
    if len(num_list)>1:
        mid = len(num_list)//2
        lefthalf = num_list[:mid]
        righthalf = num_list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                num_list[k]=lefthalf[i]
                i=i+1
            else:
                num_list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            num_list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            num_list[k]=righthalf[j]
            j=j+1
            k=k+1

input_list=input('Enter numbers of list separated by space : ').split()
num_list=[]
for num in input_list:
    num_list.append(int(num))
n=len(num_list)-1
mergeSort(num_list) 
print('MergeSorted list : ',num_list)