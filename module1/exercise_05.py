# Group members:
# Aman Kumar
# Ian York
# Nikolas Bogolis
# Zoey Vail
# Gabriel Van Dreel
# Author: Zoey Vail

firstList = []
secondList = []
for i in range(5):
    number = input('Enter a number for the first list: ')
    firstList.append(number)
for i in [0, 1, 2, 3, 4]:
    number = input('Enter a number for the second list: ')
    secondList.append(number)
thirdList = []
for i in [0, 1, 2, 3, 4]:
    a = firstList[i]
    for r in [0, 1, 2, 3, 4]:
        if a == secondList[r]:
            thirdList.append(a)
print('First list ', firstList)
print('Second list ', secondList)
print('Common list ', thirdList)
