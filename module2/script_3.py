# By: Gabriel Van Dreel

def count_letters(s):
    letters = {}
    for ch in s.replace(' ', ''):
        if ch in letters:
            letters[ch] += 1
        else:
            letters[ch] = 1
    
    return letters

print(count_letters(input('Enter a string:')))
