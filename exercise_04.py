# Group members:
# Aman Kumar
# Ian York
# Nikolas Bogolis
# Zoey Vail
# Gabriel Van Dreel
# Author: Ian York

x = input("Enter a number: ")
z = 1
l = []
numofelem = x
while(x>0):
   y = float(input("Enter number " + str(z) + ": "))
   l.append(y)
   x = x-1
   z = z+1
print("List: " + str(l))
count = len(l)
count = count - 1
sum = 0.0
while(count>=0):
   lisval = l[count]
   sum = float(sum) + float(lisval)
   count = count - 1
average = sum/float(numofelem)
print("Average: " + str(average))
