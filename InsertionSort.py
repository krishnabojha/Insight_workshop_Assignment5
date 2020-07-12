############ Insertion sort
def insertion_Sort(int_list): 
      for i in range(1, len(int_list)): 
  
        current_value = int_list[i] 
        j = i-1
        while j >= 0 and current_value < int_list[j] : 
                int_list[j + 1] = int_list[j] 
                j -= 1
        int_list[j + 1] = current_value 
   
num_list=input('Enter numbers of list separated by space : ').split()
int_list=[]
for num in num_list:
    int_list.append(int(num))
insertion_Sort(int_list) 
print ('sorted list : ',int_list) 