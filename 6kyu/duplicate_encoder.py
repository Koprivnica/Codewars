"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character
appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization
when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
"""


def duplicate_encode(word):
    word = word.upper()
    char_dict = {}
    for char in word:
        char_dict[char] = char_dict.get(char, 0) + 1
    
    return "".join(["(" if char_dict[a] < 2 else ")" for a in word])


print(duplicate_encode("(( @"))