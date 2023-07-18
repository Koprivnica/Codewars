"""
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string
is valid, and false if it's invalid.
All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False

"""


BRACES_DICT = {"}":"{", "]":"[", ")":"("}

def valid_braces(string):
    braces_list = []
    for brace in string:
        if braces_list == [] or brace in "{[(" or braces_list[-1] != BRACES_DICT[brace]:
            braces_list.append(brace)
        else:
            braces_list.pop()
        
    return braces_list == []


print(valid_braces("(){}[]"))