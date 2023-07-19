"""
In this kata you're given an n x n array and you're expected to traverse the elements diagonally from the bottom right to the top left.

Example
  1 6 7
  7 2 4
  3 5 9

your solution should return elements in the following order
9
4 5
7 2 3
6 7
1

//=> [9, 4, 5, 7, 2, 3, 6, 7, 1]

Your task is to write the function diagonal() that returns the array elements in the above manner.

Another Example
arr = [
 [4, 5, 7],
 [3, 9, 1],
 [7, 6, 2]
]

diagonal(arr) //=> [2, 1, 6, 7, 9, 7, 5, 3, 4]
You can assume the test cases are well formed.
"""

example = [
 [4, 5, 7],
 [3, 9, 1],
 [7, 6, 2]
]


def diagonal(ar):
    n = len(ar)
    result = []
    row, col = n-1, n-1
    while row >= 0 and col >= 0:
        i, j = row, col
        temp = []
        while i >= 0 and j < n:
            temp.append(ar[i][j])
            i -= 1
            j += 1
        if col == 0:
            row -= 1
        else:
            col -= 1
        result.extend(temp[::-1])
            
    return result



print(diagonal(example))