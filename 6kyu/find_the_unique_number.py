"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains at least 3 numbers.
The tests contain some very huge arrays, so think about performance.
"""


def unique_number(arr):
    arr_dict = {}
    for elem in arr:
        if elem in arr_dict:
            arr_dict[elem] += 1
        else:
            arr_dict[elem] = 1
    
        if (len(arr_dict) == 2) and (len(set(arr_dict.values())) == 2):
            return min(arr_dict, key = arr_dict.get)

print(unique_number([1, 1, 1, 2, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
