# By: Gabriel Van Dreel

s = input('Enter a string:').replace(' ', '')
lower = ''
upper = ''
for i in range(len(s)):
    if ord(s[i]) < 91:
        upper += s[i]
    else:
        lower += s[i]
print(lower + upper)
