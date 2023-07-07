"""
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.

Examples:
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""


def finding_the_odd_int(array):
    num_dict = {}
    for num in array:
        num_dict[num] = num_dict.get(num, 0) + 1
        
    return [key for key, value in num_dict.items() if value % 2 != 0]


print(finding_the_odd_int([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))