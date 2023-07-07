"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should
have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Example:
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"""


def order(string_input):
    string_new = []
    string_input = string_input.split()
    for i in range(1, len(string_input) + 1):
        for word in string_input:
            if str(i) in word:
                string_new.append(word)
                
    return " ".join(string_new)





def order2(string_input):
    return ' '.join(sorted(string_input.split(), key=lambda w:sorted(w)))
        
    
    
        



print(order2("is2 Thi1s T4est 3a"))