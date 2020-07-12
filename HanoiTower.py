#######Tower of Hanoi problem for ‘n’ number of disks
def HanoiTower(n , rod1, rod3, rod2):
   if n == 1:
      print ("Move disk 1 from rod",rod1,"to rod",rod3)
      return
   HanoiTower(n-1, rod1, rod2, rod3)
   print ("Move disk",n,"from rod",rod1,"to rod",rod3)
   HanoiTower(n-1, rod2, rod3, rod1)
# main
n = int(input('Enter number of disk : '))
print('The steps to solve problems are : ')
HanoiTower(n, 'A', 'C', 'B')