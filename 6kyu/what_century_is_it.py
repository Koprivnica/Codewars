"""
Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.

Examples
"1999" --> "20th"
"2011" --> "21st"
"2154" --> "22nd"
"2259" --> "23rd"
"1124" --> "12th"
"2000" --> "20th"
"""


def what_century(year):
    century = (int(year) + 99) // 100
    if century // 10 != 1:
        if century % 10 == 1:
            return f"{century}st"
        elif century % 10 == 2:
            return f"{century}nd"
        elif century % 10 == 3:
            return f"{century}rd"
        else:
            return f"{century}th"
    return f"{century}th"


print(what_century("2000"))