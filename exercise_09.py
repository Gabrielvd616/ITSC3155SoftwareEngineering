# Group members:
# Aman Kumar
# Ian York
# Nikolas Bogolis
# Zoey Vail
# Gabriel Van Dreel
# Author: Nikolas Bogolis

words = [] # Initialize a list named words.

for i in range(1,6): # Prompts the user to input 5 words.
	print("Enter a word: ".format(i),end="")
	words.append(input()) # Adds each word to the list words.

print("Words: " + str(words)) # Displays the initial list of words.

words_string = ' '.join(str(x) for x in words) # Converts each string of text in words adds a space in between as one string.

print("One String: " + words_string) # Displays the result of a single string from list.
