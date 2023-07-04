"""
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct
letters - each taken only once - coming from s1 or s2.
"""

def longest(string1, string2):
    
    # The function first concatenates both strings, than creates a set in order to remove duplicates.
    # After that the set i sorted and again converted to a string
    
    return "".join(sorted(set(string1 + string2)))