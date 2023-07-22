"""
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the
integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return
the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and
Result<Vec<u32>, String> in Rust).

Example:
divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
"""


def divisors(integer):
    end_point = int(integer**0.5) + 1
    result = set([])
    for num in range(2, end_point):
        if integer % num == 0:
            result.add(num)
            result.add(integer // num)
    if not result:
        return f"{integer} is prime"
    return sorted(result)


print(divisors(25))