# By: Gabriel Van Dreel

import copy

def get_combined_dict(dict_1, dict_2):
    new_dict = copy.deepcopy(dict_1)
    for key in dict_1:
        if key in dict_2:
            new_dict[key] += dict_2[key]
        else:
            new_dict.pop(key)
    
    return new_dict

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
