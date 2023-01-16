# By: Gabriel Van Dreel

li = []
i = 0
while i < 5:
    try:
        li.append(int(input(f'Enter int #{i + 1}:')))
        i += 1
    except ValueError as e:
        print('Invalid input. Please enter an int.')
    except:
        e = sys.exc_info()[0]
        print(e)

print('Your sum is', sum(li))