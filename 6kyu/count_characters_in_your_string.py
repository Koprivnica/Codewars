"""
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the
result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""


def count(s):
    count_dict = {}
    for char in s:
        count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict


print(count("aba"))