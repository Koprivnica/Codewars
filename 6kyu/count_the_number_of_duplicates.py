"""
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than
once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""


def duplicate_count(text):
    counter = 0
    char_dict = {}
    for char in text.upper():
        char_dict[char] = char_dict.get(char, 0) + 1
        if char_dict[char] == 2:
            counter += 1
            
    return counter


print(duplicate_count("abcde"))