# Group members:
# Aman Kumar
# Ian York
# Nikolas Bogolis
# Zoey Vail
# Gabriel Van Dreel
# Author: Nikolas Bogolis

string = input("Enter a string: ") # Prompts the user for input.

lst = list(string) # Converts the inputted string into a list.

tri_list = [lst[i:i + 3] for i in range(0, len(lst), 3)] # Moves 3 elements from the first list into their own lists.

print(tri_list) # Displays the result.
