########### Bubble sort
def bubble_Sort(int_list):
    for a in range(len(int_list)-1,0,-1):
        for i in range(a):
            if int_list[i]>int_list[i+1]:
                temp = int_list[i]
                int_list[i] = int_list[i+1]
                int_list[i+1] = temp

nlist = input('Enter numbers of list separated by space : ').split()
int_list=[]
for num in nlist:
    int_list.append(int(num))
bubble_Sort(int_list)
print('Sorted list : ',int_list)