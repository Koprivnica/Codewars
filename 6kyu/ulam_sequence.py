"""
The Ulam sequence U is defined by u0 = u, u1 = v, with the general term uN for N > 2 given by the least integer expressible uniquely as
the sum of two distinct earlier terms. In other words, the next number is always the smallest, unique sum of any two previous terms.
Complete the function that creates an Ulam Sequence starting with the given u0 and u1, and contains n terms.

Example
The first 10 terms of the sequence U(u0=1, u1=2) are: 1, 2, 3, 4, 6, 8, 11, 13, 16, 18.

Let's see it in details:

    The first term after the initial 1, 2 is obviously 3, because 1 + 2 = 3
    The next term is 1 + 3 = 4 (we don't have to worry about 4 = 2 + 2 since it is a sum of a single term instead of distinct terms)
    5 is not a member of the sequence since it is representable in two ways: 1 + 4 and 2 + 3
    6 is a memeber, as 2 + 4 = 6
"""


def ulam_sequence(u0, u1, n):
    """
    u0 = first number
    u1 = second numberr
    n  = final number of elements in the sequence
    """
    sequence = [u0, u1]
    sums_dict = {}
    while len(sequence) < n:
        for i in range(0, len(sequence)-1):
            sum = sequence[i] + sequence[-1]
            sums_dict[sum] = sums_dict.get(sum, 0) + 1
        min_sum = min([key for key, value in sums_dict.items() if value == 1])
        sequence.append(min_sum)
        del sums_dict[min_sum]
    
    return sequence


print(ulam_sequence(3,4,5))