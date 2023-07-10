"""
Kevin is noticing his space run out! Write a function that removes the spaces from the values and returns an array showing the space
decreasing.
For example, running this function on the array ['i', 'have','no','space'] would produce ['i','ihave','ihaveno','ihavenospace']
"""


def deacreasing_space(array):
    string = ""
    new_array = []
    for elem in array:
        string = string + elem
        new_array.append(string)
    
    return new_array


print(deacreasing_space(['i', 'have','no','space']))