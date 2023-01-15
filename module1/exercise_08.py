# Group members:
# Aman Kumar
# Ian York
# Nikolas Bogolis
# Zoey Vail
# Gabriel Van Dreel
# Author: Gabriel Van Dreel

arr = []
arr_once = []
s = set()
for i in range(10):
    arr.append(int(input('Enter number ' + str(i + 1) + ':')))
    if arr[i] in s:
        if arr[i] in arr_once:
            arr_once.remove(arr[i])
    else:
        arr_once.append(arr[i])
        s.add(arr[i])

print('Original List:', arr)
print('Nums that appear once:', arr_once)
