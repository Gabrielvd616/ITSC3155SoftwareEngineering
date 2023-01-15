# Group members:
# Aman Kumar
# Ian York
# Nikolas Bogolis
# Zoey Vail
# Gabriel Van Dreel
# Author: Zoey Vail

r = input('Row - Enter a number between 1 and 5: ')
c = input('Column - Enter a number between 1 and 5: ')
row = int(r) - 1
column = int(c) - 1
arr = [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]
arr[row][column] = 1
for i in range(5):
    print(arr[i])
