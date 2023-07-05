# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd,
# return the middle character. If the word's length is even, return the middle 2 characters.


def get_middle_char(in_string):
    str_len = len(in_string)
    if str_len % 2 != 0:
        return in_string[str_len // 2]
    return in_string[(str_len // 2) - 1 : (str_len // 2) + 1]


"""
very cool solution from codewars
def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s
"""